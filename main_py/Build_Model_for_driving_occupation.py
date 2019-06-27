import pickle
import json
import numpy as np
import keras
import Label_Constant as lc
from keras.models import load_model
import numpy as np
def data_generator(training_x,training_y, batch_size):
    data_len = len(training_x)

    package_num = int(data_len / batch_size)
    idx = np.arange(package_num)
    np.random.shuffle(idx)
    while True:
        for i in idx:
            x = training_x[i*package_num:(i+1)*package_num]
            y = training_y[i*package_num:(i+1)*package_num]
            yield (x,y)
def pad_vec_sequence(vec_sequences, max_len,pad_value = 0, vec_length=768):
    for vec_sequence in vec_sequences:
        for i in range(len(vec_sequence), max_len):
            vec_sequence.append(pad_value)
    return np.asarray(vec_sequences)


verdict_count = 10000

training_verdict_list = pickle.load(open('../embed_verdict/unsafe_driving_'+str(verdict_count)+'.emb', 'rb'))
word_set_dict = pickle.load(open('../embed_verdict/fcs_word_set.dic', 'rb'))
word_to_index_dict = pickle.load(open('../embed_verdict/fcs_word_index.dic','rb'))
index_to_word_dict = pickle.load(open('../embed_verdict/fcs_index_word.dic','rb'))
word_number = len(word_set_dict[lc.driving_occupation_code])
training_x = []
training_y = []

max_len = 0
for i,verdict in enumerate(training_verdict_list):
    input_x = []
    if lc.driving_occupation_context in verdict.keys():
        for sen in verdict[lc.driving_occupation_context]:
            input_x.extend([word_to_index_dict[lc.driving_occupation_code][word] for word in sen if word in word_to_index_dict[lc.driving_occupation_code].keys()])

        if len(input_x) > max_len:
            max_len = len(input_x)
        training_x.append(input_x)
        training_y.append(verdict['label_vector'][lc.driving_occupation_vec_index:lc.driving_occupation_vec_index+lc.driving_occupation_vec_len])
    if verdict[lc.driving_occupation_code]=='1':
        for j in range(10):
            training_x.append(input_x)
            training_y.append(verdict['label_vector'][
                              lc.driving_occupation_vec_index:lc.driving_occupation_vec_index + lc.driving_occupation_vec_len])

print(max_len)

training_x = pad_vec_sequence(training_x,max_len)
training_y = np.asarray(training_y)
print(training_x)
print(training_y)
print(training_x.shape)
print(training_y.shape)

label_count = dict()
for i in range(2):
    label_count[i] = 0
for y in training_y:
    label_count[y[0]] +=1
print(label_count)

#mask_vec = np.zeros(768, dtype='float64')

model = keras.Sequential()
model.add(keras.layers.Embedding(word_number,300,mask_zero=True))
model.add(keras.layers.SpatialDropout1D(0.2))
model.add(keras.layers.LSTM(300))
model.add(keras.layers.Activation('relu'))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(1))

model.add(keras.layers.Activation('sigmoid'))
binary_loss = 'binary_crossentropy'
categorical_loss = 'categorical_crossentropy'
model.compile(optimizer='adam', loss=binary_loss, metrics=['accuracy'])

data_length = len(training_x)

batch_size = 5
#model = load_model('../model/driving_occupation.h5')

model.fit(training_x,training_y,validation_split = 0.1,epochs = 5)
model.save('../model/driving_occupation.h5')
#del(model)
model = load_model('../model/driving_occupation.h5')
result = model.predict([training_x])
correct_count = 0
for i,single in enumerate(result):
    print(single,training_y[i])
    if single[0] > lc.driving_occupation_threshold:
        re = 1.0
    else:
        re = 0.0
    if re == training_y[i][0]:
        correct_count+=1
    print(re,':',training_y[i][0])
print(correct_count/len(training_x))
