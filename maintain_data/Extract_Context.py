import pickle
import Label_Constant as lc
from bert_embedding import BertEmbedding

def build_dic(word_set):
    word_to_index = dict()
    index_to_word = dict()
    word_to_index['UNK'] = 1
    word_to_index['MSK'] = 0
    index_to_word[0] = 'MSK'
    index_to_word[1] = 'UNK'
    for word in word_set:
        word_to_index[word] = len(word_to_index)
        index_to_word[len(index_to_word)] = word

    return word_to_index,index_to_word
verdict_count = 10000
verdict_list = pickle.load(open('../factor_training_data/unsafe_driving_'+str(verdict_count)+'.emb','rb'))
bert_embedding = BertEmbedding(model='bert_12_768_12', dataset_name='wiki_cn_cased')
word_set_dict = dict()


for verdict_count,verdict in enumerate(verdict_list):
    print(verdict_count)
#rule
    if lc.alcohol_code in verdict.keys():
        if lc.alcohol_code not in word_set_dict.keys():
            word_set_dict[lc.alcohol_code] = set()
        for i,sen in enumerate(verdict['text']):
            is_finded = False
            for key_word in lc.alcohol_key_words:
                if key_word in sen:
                    context = verdict['text'][i:i+1]
                    for single_context in context:
                        single_context = single_context.replace(' ','')
                        for char in single_context:
                            word_set_dict[lc.alcohol_code].add(char)
                    verdict[lc.alcohol_context] = context
                    is_finded = True
                    break
            if is_finded:
                break
#ML
    if lc.accident_code in verdict.keys():
        if lc.accident_code not in word_set_dict.keys():
            word_set_dict[lc.accident_code] = set()
        for i,sen in enumerate(verdict['text']):
            is_finded = False
            for key_word in lc.accident_key_words:
                if key_word in sen:

                    context = verdict['text'][i:i + 1]
                    for single_context in context:
                        single_context = single_context.replace(' ', '')
                        for char in single_context:
                            word_set_dict[lc.accident_code].add(char)
                    verdict[lc.accident_context] = context
                    is_finded = True
                    break
            if is_finded:
                break
#ML
    if lc.vehicle_code in verdict.keys():
        if lc.vehicle_code not in word_set_dict.keys():
            word_set_dict[lc.vehicle_code] = set()
        for i,sen in enumerate(verdict['text']):
            is_finded = False
            for key_word in lc.vehicle_key_words:
                if key_word in sen:
                    context = verdict['text'][i:i + 1]
                    for single_context in context:
                        while ' ' in single_context:
                            single_context = single_context.replace(' ', '')
                        for char in single_context:
                            word_set_dict[lc.vehicle_code].add(char)
                    verdict[lc.vehicle_context] = context
                    is_finded = True
                    break
            if is_finded:
                break
#key word
    if lc.violate_property_code in verdict.keys():
        if lc.violate_property_code not in word_set_dict.keys():
            word_set_dict[lc.violate_property_code] = set()
        for i,sen in enumerate(verdict['text']):
            is_finded = False
            for key_word in lc.violate_property_key_words:
                if key_word in sen:
                    context = verdict['text'][i:i + 1]
                    for single_context in context:
                        while ' ' in single_context:
                            single_context = single_context.replace(' ', '')
                        for char in single_context:
                            word_set_dict[lc.violate_property_code].add(char)
                    verdict[lc.violate_property_context] = context
                    is_finded = True
                    break

            if is_finded:
                break
#ML
    if lc.driving_occupation_code in verdict.keys():
        if lc.driving_occupation_code not in word_set_dict.keys():
            word_set_dict[lc.driving_occupation_code] = set()
        for i,sen in enumerate(verdict['text']):
            is_finded = False
            for key_word in lc.driving_occupation_key_words:
                if key_word in sen:
                    context = verdict['text'][i:i + 1]
                    for single_context in context:
                        while ' ' in single_context:
                            single_context = single_context.replace(' ', '')
                        for char in single_context:
                            word_set_dict[lc.driving_occupation_code].add(char)
                    verdict[lc.driving_occupation_context] = context
                    is_finded = True
                    break
            if is_finded:
                break
#ML
    if lc.commit_crime_code in verdict.keys():
        if lc.commit_crime_code not in word_set_dict.keys():
            word_set_dict[lc.commit_crime_code] = set()
        for i,sen in enumerate(verdict['text']):
            is_finded = False
            for key_word in lc.commit_crime_key_words:
                if key_word in sen:
                    context = verdict['text'][i:i + 1]
                    for single_context in context:
                        while ' ' in single_context:
                            single_context = single_context.replace(' ', '')
                        for char in single_context:
                            word_set_dict[lc.commit_crime_code].add(char)
                    verdict[lc.commit_crime_context] = context
                    is_finded = True
                    break
            if is_finded:
                break
#ML
    if lc.region_code in verdict.keys():
        if lc.region_code not in word_set_dict.keys():
            word_set_dict[lc.region_code] = set()
        for i,sen in enumerate(verdict['text']):
            is_finded = False
            for key_word in lc.region_key_words:
                if key_word in sen:
                    context = verdict['text'][i:i + 1]
                    for single_context in context:
                        while ' ' in single_context:
                            single_context = single_context.replace(' ', '')
                        for char in single_context:
                            word_set_dict[lc.region_code].add(char)
                    verdict[lc.region_context] = context
                    is_finded = True
                    break
            if is_finded:
                break


word_to_index_dict = dict()
index_to_word_dict = dict()
for key in word_set_dict.keys():
    word_to_index,index_to_word = build_dic(word_set_dict[key])
    word_to_index_dict[key] = word_to_index
    index_to_word_dict[key] = index_to_word
verdict_count = 10000
pickle.dump(verdict_list,open('../embed_verdict/unsafe_driving_'+str(verdict_count)+'.emb','wb'))
pickle.dump(word_set_dict,open('../embed_verdict/fcs_word_set.dic','wb'))
pickle.dump(word_to_index_dict,open('../embed_verdict/fcs_word_index.dic','wb'))
pickle.dump(index_to_word_dict,open('../embed_verdict/fcs_index_word.dic','wb'))