import math
def cal_idf(corpus):
    total_count = len(corpus)
    word_set = set()
    word_count_dict = dict()
    for sentence in corpus:
        for word in sentence:
            word_set.add(word)

    for word in word_set:
        word_count_dict[word] = 0
        for sentence in corpus:
            if word in sentence:
                word_count_dict[word] += 1
        word_count_dict[word] = math.log(total_count/word_count_dict[word])
    return word_count_dict

def is_stopword(term,stopword_list,punctuation_list,stopunit_list):
    if term not in punctuation_list and str(term) not in stopword_list:
        not_unit = True
        for stopunit in stopunit_list:
            if stopunit in term:
                not_unit = False
        if not_unit:
            return True
        else:
            return False
    return False
