import jieba
import Label_Constant as lc
import numpy as np

def predict(text):
    alocohol_vec = np.zeros(lc.alcohol_vec_len,dtype=np.int)
    value = -1
    if text is None:
        return alocohol_vec
    elif len(text) == 0:
        return alocohol_vec
    for seg in jieba.cut(text):
        try:
            value = float(seg)
        except:
            pass
    alcohol_concentration = value
    if alcohol_concentration <= 0.24:
        alcohol_index = 0
    elif 0.24 < alcohol_concentration <= 0.54:
        alcohol_index = 1
    elif 0.54 < alcohol_concentration <= 0.74:
        alcohol_index = 2
    elif 0.74 < alcohol_concentration <= 0.99:
        alcohol_index = 3
    elif 0.99 < alcohol_concentration <= 1.49:
        alcohol_index = 4
    elif 1.49 < alcohol_concentration <= 1.99:
        alcohol_index = 5
    elif alcohol_concentration > 1.99:
        alcohol_index = 6
    alocohol_vec[alcohol_index] = 1
    return [alocohol_vec]

if __name__ == '__main__':
    text = '對其測得其當時吐氣酒精濃度高達每公升1.09毫克'
    print(predict(text))