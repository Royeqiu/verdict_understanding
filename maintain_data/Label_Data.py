import pickle
import random
from os import listdir
import Verdict
import jieba
import NLP_function
from maintain_data.Feature_Loader import Feature_Loader

def tokenize(verdict):
    verdict_content = verdict.get_main_content()
    people_name = verdict.get_people_name()
    if people_name is not None:
        verdict_content = verdict_content.replace(people_name, '')
    if verdict_content is not None:
        main_content_tokens = [str(term) for term in jieba.cut(verdict_content) \
                        if NLP_function.is_stopword(term, feature_loader.stopword_list,
                                                    feature_loader.punctuation_list,
                                                    feature_loader.stopunit_list)]
    else:
        main_content_tokens = []

    return main_content_tokens

root = '../data/'
dic = '../dic/'
positive_data = []
negative_data = []
feature_loader = Feature_Loader(dic)
jieba.load_userdict('../dic/userdic')

for folder_name in listdir(root):
    for file_name in listdir(root + folder_name):
        total_name = root + folder_name + '/' + file_name
        verdict = Verdict.Verdict(total_name)
        main_content_tokens = tokenize(verdict)
        if Verdict.is_unsafe_driving(verdict.json_verdict):
            tmp_dict = dict()
            tmp_dict['data'] = main_content_tokens
            tmp_dict['label'] = 1
            positive_data.append(tmp_dict)
        else:
            tmp_dict = dict()
            tmp_dict['data'] = main_content_tokens
            tmp_dict['label'] = 0
            negative_data.append(tmp_dict)
training_data = [single_data for single_data in positive_data]
random.shuffle(negative_data)
for i in range(0,len(positive_data)):
    training_data.append(negative_data[i])
random.shuffle(training_data)
file=open('../training_data/unsafe_driving.pkl','wb')
pickle.dump(training_data,file)
file.close()