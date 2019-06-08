import json
import Verdict
from os import listdir
import jieba
import NLP_function
import numpy
from maintain_data.Feature_Loader import Feature_Loader

def extract_feature(idf_dict):
    mean = numpy.mean([value for value in idf_dict.values()])
    std = numpy.std(sorted(idf_dict.values()))
    threshold = mean - 2 * std
    feature = [str(item) for item in sorted(idf_dict.items(), key=lambda d: d[1]) if item[1] < threshold]
    return feature

if __name__ == '__main__':
    feature_loader = Feature_Loader()
    jieba.load_userdict('dic/userdic')
    root = 'data/'
    verdict_list = []
    corpus = []
    for folder_name in listdir(root):
        for file_name in listdir(root + folder_name):
            total_name = root + folder_name + '/' + file_name
            verdict = Verdict.Verdict(total_name)
            if Verdict.is_unsafe_driving(verdict.json_verdict):
                unsafe_drive_verdict = Verdict.Unsafe_Driving(total_name)
                verdict_content = unsafe_drive_verdict.get_main_content()
                people_name = unsafe_drive_verdict.get_people_name()
                if people_name is not None:
                    verdict_content = verdict_content.replace(people_name,'')
                if verdict_content is not None:
                    corpus.append([str(term) for term in jieba.cut(verdict_content) \
                                   if NLP_function.is_stopword(term,feature_loader.stopword_list,feature_loader.punctuation_list,feature_loader.stopunit_list)])
                else:
                    corpus.append('')
                verdict_list.append(unsafe_drive_verdict)
            else:
                other_verdict = verdict
    idf_dict = NLP_function.cal_idf(corpus)
    feature = extract_feature(idf_dict)
    feature_file = open('pre_training_feature/unsafe_driving.fea', 'w')
    feature_file.write(json.dumps(feature, ensure_ascii=False))


