import pickle
import json
import jieba
import NLP_function
from maintain_data.Feature_Loader import Feature_Loader
from sklearn.linear_model import LogisticRegression
from maintain_data.Feature_Transformer import Feature_Transformer
from Verdict import Verdict

dic = '../dic/'
jieba.load_userdict(dic+'userdic')
ft = pickle.load(open('../train_feature/ft_unsafe_driving.pkl','rb'))
feature_loader = Feature_Loader(dic)
logreg = pickle.load(open('../model/unsafe_driving.mod','rb'))


def analyze(verdict):

    verdict_content = verdict.get_main_content()
    test_input = ft.turn_index_to_one_hot([str(term) for term in jieba.cut(verdict_content) if NLP_function.is_stopword(term,feature_loader.stopword_list,feature_loader.punctuation_list,feature_loader.stopunit_list)])

    return logreg.predict([test_input])[0]

if __name__ == '__main__':

    test_data = open('../test_case.json', 'r', encoding='utf-8')
    json_verdict = json.load(test_data)
    print('Verdict Feature:')
    print(ft.feature_to_index)
    test_verdict = Verdict(json_verdict)
    print('Unsafe Driving Feature:')
    json_feature = json.load(open('../pre_training_feature/unsafe_driving.fea', 'r', encoding='utf-8'))
    print(json_feature)
    print(test_verdict.get_people_name())
    print(test_verdict.get_main_content())
    print('是否是不能安全駕駛:')
    print(analyze(test_verdict))
