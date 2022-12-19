
# anonymize_text('John is old')
print(len('XXXXXXXXXXX'))
print(len('Mark Oldham'))

import spacy

nlp = spacy.load("en_core_web_sm")


def anonymize_text(sentences):
    doc = nlp(sentences)
    persons = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    checkLen = [int(len(x)) for x in persons]
    sentences = list(sentences)
    temp = []
    for i in range(len(sentences)):
        for j in range(len(checkLen)):
            pivot = checkLen[j]
            if 0 <= i + pivot - 1 <= len(sentences):
                temp = "".join(sentences[i:i + pivot])
                if temp in persons:
                    for k in range(i, i + pivot):
                        sentences[k] = 'X'

    return "".join(sentences)