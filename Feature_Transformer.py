import NLP_Constant
import json
import numpy

class Feature_Transformer:
    def __init__(self):
        self.feature_to_index = dict()
        self.index_to_feature = dict()

    def load_feature(self,filepath):
        with open(filepath,'r',encoding='utf-8') as op:
            json_feature = json.load(op)
        self.feature_to_index[NLP_Constant.unknown_term] = 0
        self.index_to_feature[0] = NLP_Constant.unknown_term
        for feature_pair in json_feature:
            self.feature_to_index[feature_pair[0]] = len(self.feature_to_index)
            self.index_to_feature[len(self.index_to_feature)] = feature_pair[0]

    def turn_index_to_one_hot(self,word_list):
        one_hot_vec = numpy.zeros(len(self.feature_to_index))
        for word in word_list:
            if word in self.feature_to_index.keys():
                one_hot_vec[self.feature_to_index[word]] = 1
            else:
                one_hot_vec[0] = 1
        return one_hot_vec


