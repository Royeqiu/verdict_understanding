import pickle
from keras.models import load_model
import Label_Constant as lc
import re
import json
from Verdict import Verdict
import numpy as np
from main_py import Build_Model_for_alocohol as alocohol_model
from main_py import Build_Model_for_violate_property as violate_property_model

word_set = pickle.load(open('../embed_verdict/fcs_word_set.dic','rb'))
word_to_index_dic = pickle.load(open('../embed_verdict/fcs_word_index.dic','rb'))
index_to_word_dic = pickle.load(open('../embed_verdict/fcs_index_word.dic','rb'))

accident_model = load_model(lc.model_path + lc.accident_model_name)
vehicle_model = load_model(lc.model_path + lc.vehicle_model_name)
driving_occupation_model = load_model(lc.model_path + lc.driving_occupation_model_name)
commit_crime_model = load_model(lc.model_path + lc.commit_crime_model_name)
region_model = load_model(lc.model_path + lc.region_model_name)
model_list = [alocohol_model,vehicle_model,region_model,accident_model,violate_property_model,driving_occupation_model,commit_crime_model]


def pad_vec_sequence(vec_sequences, max_len,pad_value = 0, vec_length=768):
    for vec_sequence in vec_sequences:
        for i in range(len(vec_sequence), max_len):
            vec_sequence.append(pad_value)
    return np.asarray(vec_sequences)

def split_content(verdict_content):

    verdict_content = verdict_content.replace('\r\n', '')
    while '  ' in verdict_content:
        verdict_content = verdict_content.replace('  ', ' ')
    verdict_content = verdict_content.replace('\u3000', '')
    total_sen = re.split('事實|事    實', verdict_content)
    tmp_text = ''
    for i in range(1, len(total_sen)):
        tmp_text += total_sen[i]
    verdict_content = tmp_text
    sentences = [sentence for i,sentence in enumerate(re.split('。|，|：|；|\uf6b1|\uf6b2|\uf6b3|\uf6b4|\uf6b5|\uf6b6|\uf6b7|\uf6b8|事實|事    實', verdict_content)) if len(sentence) != 0 and i != 0]

    return sentences

def turn_index_to_vec(result_list):
    vec_list = []
    for index, result in enumerate(result_list):
        if result is not None:
            if len(result[0])==1:
                if result[0][0]>lc.factor_threshold_list[index]:
                    re = 1
                else:
                    re = 0
                vec_list.append(re)
            else:
                predict_index = np.argmax(result[0])
                predict_vec = np.zeros(lc.factor_vec_len_list[index],dtype=np.int)
                predict_vec[predict_index] = 1
                vec_list.extend(predict_vec.tolist())
        else:
            for i in range(lc.factor_vec_len_list[index]):
                vec_list.append(0)
    return vec_list

def get_prdict_result(padded_encode_dict,target_text_dict):
    result_list = []
    for factor_index, factor_code in enumerate(lc.factor_code_list):
        if lc.factor_is_ml_model_list[factor_index]:
            result_list.append(model_list[factor_index].predict(np.asarray([padded_encode_dict[factor_code]])))
        else:
            result_list.append(model_list[factor_index].predict(target_text_dict[lc.factor_code_list[factor_index]]))

    return result_list



def padding_facotr_encode(text_encode_dict):
    for i, factor_code in enumerate(lc.factor_code_list):
        if lc.factor_max_len_list[i] != 0:
            if text_encode_dict[factor_code] is not None:
                pad_vec_sequence([text_encode_dict[factor_code]],lc.factor_max_len_list[i])
    return text_encode_dict


def get_target_text(verdict_sentences):
    target_text_dict = dict()
    for factor_code in lc.factor_code_list:
        target_text_dict[factor_code] = None
    for sen in verdict_sentences:
        for factor_index,key_word_list in enumerate(lc.factor_key_words_list):
            for key_word in key_word_list:
                if key_word in sen:
                    if target_text_dict[lc.factor_code_list[factor_index]] is None:
                        target_text_dict[lc.factor_code_list[factor_index]] = sen
                    break
    return target_text_dict

def get_encoding(target_text_dict):
    text_encode_dict = dict()
    for factor_code in target_text_dict.keys():
        if target_text_dict[factor_code] is not None:
            text_encode_dict[factor_code] = []
            for word in target_text_dict[factor_code]:
                if len(word)==0 or word ==' ':
                    continue
                if word in word_to_index_dic[factor_code].keys():
                    text_encode_dict[factor_code].append(word_to_index_dic[factor_code][word])
                else:
                    text_encode_dict[factor_code].append(word_to_index_dic[factor_code]['UNK'])
        else:
            text_encode_dict[factor_code] = None
    return text_encode_dict

def extract_factor(verdict):
    verdict.get_all_text()
    verdict_sentences = split_content(verdict.get_all_text())
    target_text_dict = get_target_text(verdict_sentences)
    text_encode_dict = get_encoding(target_text_dict)
    padded_encode_dict = padding_facotr_encode(text_encode_dict)
    result_list = get_prdict_result(padded_encode_dict,target_text_dict)
    result_vec = turn_index_to_vec(result_list)
    return result_vec

if __name__ == '__main__':
    test_data = open('../test_case.json', 'r', encoding='utf-8')
    json_verdict = json.load(test_data)
    test_verdict = Verdict(json_verdict)
    result_vec = extract_factor(test_verdict)
    print(result_vec)