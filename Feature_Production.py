import json
import Verdict
from os import listdir
import jieba
import NLP_function
import numpy

if __name__ == '__main__':
    jieba.load_userdict('dic/userdic')
    punctuation_list = []
    with open('dic/punctuation','r',encoding='utf-8') as op:
        punctuation_str = op.readline()
        for punctuation in punctuation_str:
            punctuation_list.append(punctuation)
        op.close()
    stopword_list = []
    with open('dic/stopword','r',encoding='utf-8') as op:
        for stopword in op:
            stopword_list.append(stopword.strip('\n'))
        op.close()
    stopunit_list = []
    with open('dic/stopunit','r',encoding='utf-8') as op:
        for stopunit in op:
            stopunit_list.append(stopunit.strip('\n'))
        op.close()
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
                """
                                print(total_name)
                                print(unsafe_drive_verdict.get_title())
                                print(verdict_content)
                                print(unsafe_drive_verdict.get_people_name())
                                """
                if verdict_content is not None:
                    corpus.append([str(term) for term in jieba.cut(verdict_content) \
                                   if NLP_function.is_stopword(term,stopword_list,punctuation_list,stopunit_list)])
                else:
                    corpus.append('')
                verdict_list.append(unsafe_drive_verdict)
    idf_dict = NLP_function.cal_idf(corpus)
    mean = numpy.mean([value for value in idf_dict.values()])
    std = numpy.std(sorted(idf_dict.values()))
    threshold = mean-2*std
    feature_file = open('feature/unsafe_driving.fea', 'w')
    feature = [str(item) for item in sorted(idf_dict.items(), key=lambda d: d[1]) if item[1] < threshold]
    feature_file.write(json.dumps(feature, ensure_ascii=False))


