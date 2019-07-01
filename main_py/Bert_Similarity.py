from NLP.NLP_Tool import NLP_Tool

bert = NLP_Tool(load_spacy_model=False, load_bert_model=True)




term_list = [['毫','克']]
term_vector = []
result = bert.bert(['毫克'])
"""
for term in term_list:
    for word in term:
        if
"""
for index, word_set in enumerate(result):
    print(word_set[0])
    print(word_set[1])
    print()


