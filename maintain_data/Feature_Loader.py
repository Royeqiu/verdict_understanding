
class Feature_Loader():

    def __init__(self,dic_path ='dic/'):
        punctuation_list, stopword_list, stopunit_list = self.load_dict(dic_path)
        self.punctuation_list = punctuation_list
        self.stopword_list = stopword_list
        self.stopunit_list = stopunit_list

    def load_dict(self,dic_path):
        punctuation_list = []
        with open(dic_path+'punctuation', 'r', encoding='utf-8') as op:
            punctuation_str = op.readline()
            for punctuation in punctuation_str:
                punctuation_list.append(punctuation)
            op.close()
        stopword_list = []
        with open(dic_path+'stopword', 'r', encoding='utf-8') as op:
            for stopword in op:
                stopword_list.append(stopword.strip('\n'))
            op.close()
        stopunit_list = []
        with open(dic_path+'stopunit', 'r', encoding='utf-8') as op:
            for stopunit in op:
                stopunit_list.append(stopunit.strip('\n'))
            op.close()
        return punctuation_list, stopword_list, stopunit_list

