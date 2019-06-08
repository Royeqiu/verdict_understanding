import pickle
import random
from os import listdir
import Verdict

root = '../data/'
positive_data = []
negative_data = []
for folder_name in listdir(root):
    for file_name in listdir(root + folder_name):
        total_name = root + folder_name + '/' + file_name
        verdict = Verdict.Verdict(total_name)
        if Verdict.is_unsafe_driving(verdict.json_verdict):
            tmp_dict = dict()
            tmp_dict['data'] = verdict
            tmp_dict['label'] = 1
            positive_data.append(tmp_dict)
        else:
            tmp_dict = dict()
            tmp_dict['data'] = verdict
            tmp_dict['label'] = 0
            negative_data.append(tmp_dict)
print(len(positive_data),len(negative_data))
training_data = [single_data for single_data in positive_data]
random.shuffle(negative_data)
for i in range(0,len(positive_data)):
    training_data.append(negative_data[i])
print(len(training_data))
for i in range(0,5):
    print(training_data[i])

random.shuffle(training_data)
for i in range(0,5):
    print(training_data[i])
file=open('../training_data/unsafe_driving.pkl','wb')
pickle.dump(training_data,file)
file.close()