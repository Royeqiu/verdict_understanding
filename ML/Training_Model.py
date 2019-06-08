import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np
ft = pickle.load(open('../train_feature/ft_unsafe_driving.pkl','rb'))
corpus_data = open('../training_data/unsafe_driving.pkl','rb')
training_data = pickle.load(corpus_data)

split = int(0.9 * len(training_data))
training_input = []
training_output = []
test_input = []
test_output = []
#print (training_data)
for i in range(split):
    training_input.append(ft.turn_index_to_one_hot(training_data[i]['data']))
    training_output.append(training_data[i]['label'])
for i in range(split,len(training_data)):
    test_input.append(ft.turn_index_to_one_hot(training_data[i]['data']))
    test_output.append(training_data[i]['label'])
logreg = LogisticRegression(C=1e5, solver='lbfgs')
logreg.fit(training_input,training_output)
count = 0
for i,test_data in enumerate(test_input):
    print(training_data[i+split]['data'])
    predict_result = logreg.predict([test_data])[0]
    print('預測結果:',predict_result,'真實結果:',test_output[i])
    if predict_result==test_output[i]:
        count += 1
print(len(test_input))
print(count/len(test_input))
pickle.dump(logreg,open('../model/unsafe_driving.mod','wb'))