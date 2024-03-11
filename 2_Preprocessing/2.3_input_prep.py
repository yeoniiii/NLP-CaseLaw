import hanja
import re
from nltk import sent_tokenize


def prep(sent):
    sent = hanja.translate(sent, 'substitution')
    sent = re.sub(r'\?', '.', sent)
    sent = re.sub('[^가-힣. ]', '', sent)

    return sent

def tokenize(sent):
    sent_tokened = sent_tokenize(sent)

    return sent_tokened