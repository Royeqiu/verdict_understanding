import os
import json
import re
import pickle
from maintain_data import Extract_Label as el

def load_needed_label(file_path):

    label_list = []
    with open(file_path,'r') as op:
        for data in op:
            label_list.append(data.strip('\n'))
        op.close()
    return label_list

def load_verdict_label(file_path):
    label_file_dict = dict()
    for file_name in os.listdir(file_path):
        json_label = json.load(open(file_path + '/' + file_name, encoding='utf-8'))
        label_file_dict[file_name] = json_label
    return label_file_dict

def add_text(label_file_dict,verdict_root_path):
    for key in label_file_dict.keys():
        for verdict_label in label_file_dict[key]:
            folder = key.split('.')[0]
            tmp_file = open(verdict_root_path+'/'+folder+'/'+verdict_label['filename'],'r',encoding='ANSI')
            text = ''
            for data in tmp_file:
                text += data.strip('\r\n')
            while '  ' in text:
                text = text.replace('  ',' ')
            text = text.replace('\u3000','')
            sentences = [sentence for i,sentence in enumerate(re.split('。|，|：|；|\uf6b1|\uf6b2|\uf6b3|\uf6b4|\uf6b5|\uf6b6|\uf6b7|\uf6b8',text)) if len(sentence)!=0 and i!=0]
            verdict_label['text'] = sentences
    return label_file_dict



needed_label_path = '../needed_label'
label_root_path = '../nsd-json-label'
verdict_root_path = '../nsd-json'
label_file_dict = load_verdict_label(label_root_path)
needed_label = load_needed_label(needed_label_path)
word_set = set()
label_file_dict = add_text(label_file_dict,verdict_root_path)
verdict_count = 10000
count = 0
embed_list = []
for folder in label_file_dict.keys():
    for verdict in label_file_dict[folder]:
        if 'fcs_29' not in verdict.keys():
            continue
        if int(verdict['fcs_29'])!=1:
            continue
        verdict['embedding'] = None
        for key in verdict.keys():
            if key == 'text':
                count += 1
        embed_list.append(verdict)
        print(count)
        if count > verdict_count:
            break
    if count > verdict_count:
        break
print('finish_input_embed')
print('prepare_label')
el.get_label_vector(embed_verdict_list=embed_list)
print('finish_prepare_label')
print('produce_data')
pickle.dump(embed_list,open('../factor_training_data/unsafe_driving_'+str(verdict_count)+'.emb','wb'))
print('complete_producing')