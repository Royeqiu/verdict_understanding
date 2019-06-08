from maintain_data.Feature_Transformer import Feature_Transformer
from NLP.NLP_Tool import NLP_Tool
import pickle
import numpy
import json
with open('../pre_training_feature/unsafe_driving.fea','r',encoding='utf-8') as op:
    unsafe_driving_feature = json.loads(op.readline())
    op.close()
unsafe_driving_feature=[str(feature[0]) for feature in unsafe_driving_feature]
corpus_data = open('../training_data/unsafe_driving.pkl','rb')
training_data = pickle.load(corpus_data)
corpus = []
for data in training_data:
    corpus.append(data['data'])
ft = Feature_Transformer()
nlp = NLP_Tool()
idf_dict=nlp.cal_idf(corpus)
mean = numpy.mean([value for value in idf_dict.values()])
std = numpy.std(sorted(idf_dict.values()))
low_bound = mean - (0.5 * std)
up_bound = mean + (0.5 * std)
extracted_feature = [str(item[0]) for item in sorted(idf_dict.items(), key=lambda d: d[1]) if item[1] < up_bound and item[1] > low_bound]
extracted_feature.extend(unsafe_driving_feature)
corpus.append(unsafe_driving_feature)
ft.load_corpus(corpus, extracted_feature)
pickle.dump(ft,open('../train_feature/ft_unsafe_driving.pkl','wb'))