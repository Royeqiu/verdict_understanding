
class Feature_Loader():

    def __init__(self):
        punctuation_list, stopword_list, stopunit_list = self.load_dict()
        self.punctuation_list = punctuation_list
        self.stopword_list = stopword_list
        self.stopunit_list = stopunit_list

    def load_dict(self):
        punctuation_list = []
        with open('dic/punctuation', 'r', encoding='utf-8') as op:
            punctuation_str = op.readline()
            for punctuation in punctuation_str:
                punctuation_list.append(punctuation)
            op.close()
        stopword_list = []
        with open('dic/stopword', 'r', encoding='utf-8') as op:
            for stopword in op:
                stopword_list.append(stopword.strip('\n'))
            op.close()
        stopunit_list = []
        with open('dic/stopunit', 'r', encoding='utf-8') as op:
            for stopunit in op:
                stopunit_list.append(stopunit.strip('\n'))
            op.close()
        return punctuation_list, stopword_list, stopunit_list

