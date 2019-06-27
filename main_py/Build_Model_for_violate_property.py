import numpy as np
import Label_Constant as lc
def predict(text):
    violate_property_vec = np.zeros(lc.violate_property_vec_len,dtype=np.int)
    if text is None:
        return [violate_property_vec]
    if len(text) ==0:
        return [violate_property_vec]
    else:
        violate_property_vec[0] = 1
        return [violate_property_vec]
