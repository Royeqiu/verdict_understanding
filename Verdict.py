import json
import Verdict_Constant
import NLP_Constant
from hanziconv import HanziConv
from pyhanlp import *
segment = HanLP.newSegment().enableNameRecognize(True);
class Verdict:
    def __init__(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as op:
            self.json_verdict= json.load(op)
            op.close()

    def get_title(self):
        return self.json_verdict[Verdict_Constant.verdict_constant.title]

    def get_main_content(self):
        main_content = None
        verdict_sentences = self.json_verdict[Verdict_Constant.verdict_constant.full_text].replace(Verdict_Constant.verdict_constant.newline, '').split(Verdict_Constant.verdict_constant.period)
        for i,verdict_sentence in enumerate(verdict_sentences):
            while Verdict_Constant.verdict_constant.duplicate_space in verdict_sentence:
                verdict_sentence = verdict_sentence.replace(Verdict_Constant.verdict_constant.duplicate_space, Verdict_Constant.verdict_constant.single_space)
            for content_key in Verdict_Constant.verdict_constant.main_content:
                if content_key in verdict_sentence:
                    main_content = verdict_sentence.split(content_key)[1]
                    break
            if main_content is not None:
                break
        return main_content

class Unsafe_Driving(Verdict):

    def __init__(self,filepath):
        super(Unsafe_Driving,self).__init__(filepath)

    def is_confirmed(self):
        if Verdict_Constant.unsafe_driving_constant.type_one_keyword in self.get_main_content():
            return True
        else:
            return False

    def get_people_name(self):
        term_list = segment.seg(HanziConv.toSimplified(self.get_main_content()))
        for term in term_list:
            if str(term.nature) == NLP_Constant.people_name_pos:
                return HanziConv.toTraditional(str(term.word))
        return None

def is_unsafe_driving(json_verdict): #目前只有針對第一項，酒駕項目進行處理
    if Verdict_Constant.unsafe_driving_constant.type_one_keyword \
            in json_verdict[Verdict_Constant.verdict_constant.full_text]:
        return True
    else:
        return False

