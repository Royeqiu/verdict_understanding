import os
import pickle
import json
import numpy as np
import re
import Label_Constant as lc
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
            sentences = [sentence for i,sentence in enumerate(re.split('。|\uf6b1|\uf6b2|\uf6b3|\uf6b4|\uf6b5|\uf6b6|\uf6b7|\uf6b8',text)) if len(sentence)!=0 and i!=0]
            verdict_label['text'] = sentences
    return label_file_dict

def turn_label_into_vec(verdict):
    label_vec = np.zeros(lc.vector_len)
    for key in verdict.keys():
        if key in needed_label_list:
            if key == lc.alcohol_code:
                try:
                    alcohol_concentration = float(verdict[key])
                except:
                    alcohol_concentration  = 0.0
                if  alcohol_concentration <= 0.24:
                    alcohol_index = 0
                elif 0.24< alcohol_concentration <= 0.54:
                    alcohol_index = 1
                elif 0.54 < alcohol_concentration <= 0.74:
                    alcohol_index = 2
                elif 0.74 < alcohol_concentration <= 0.99:
                    alcohol_index = 3
                elif 0.99 < alcohol_concentration <= 1.49:
                    alcohol_index = 4
                elif 1.49 < alcohol_concentration <= 1.99:
                    alcohol_index = 5
                elif alcohol_concentration > 1.99:
                    alcohol_index = 6
                label_vec[lc.alcohol_vec_index+alcohol_index] = 1
            if key == lc.vehicle_code:
                vehicle_type_index = int(verdict[key])
                label_vec[lc.vehicle_vec_index+vehicle_type_index] = 1

            if key == lc.region_code:
                region_type_index = int(verdict[key])
                label_vec[lc.region_vec_index+region_type_index] = 1

            if key == lc.accident_code:
                is_accident = int(verdict[key])
                label_vec[lc.accident_vec_index] = is_accident

            if key ==lc.violate_property_code:
                is_violate_property = int(verdict[key])
                label_vec[lc.violate_property_vec_index] = is_violate_property

            if key == lc.driving_occupation_code:
                is_driving_occupation = int(verdict[key])
                label_vec[lc.driving_occupation_vec_index] = is_driving_occupation

            if key == lc.commit_crime_code:
                is_commit_crime = int(verdict[key])
                label_vec[lc.commit_crime_vec_index] = is_commit_crime
    return label_vec


needed_label_path = '../needed_label'
label_root_path = '../nsd-json-label'
verdict_root_path = '../nsd-json'
needed_label_list = load_needed_label(needed_label_path)

def get_label_vector(embed_verdict_list):
    for verdict in embed_verdict_list:
        verdict['label_vector'] = turn_label_into_vec(verdict)
    return embed_verdict_list