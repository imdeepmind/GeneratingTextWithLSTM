import re
from bs4 import BeautifulSoup

CHARS = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i': 9,'j':10,'k':11,'l':12,'m':13,
         'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,
         'z':26,' ': 27, '--':28}

def get_character_index(ch):
    if ch in CHARS.keys():
        return CHARS[ch]
    else:
        return CHARS['--']
def get_character_from_index(indx):
    for key, ind in CHARS.items():
        if ind == indx:
            return key
    return '--'

def character_to_number(text):
    return [get_character_index(c) for c in text]

def number_to_character(text):
    return ''.join([get_character_from_index(c) for c in text])

def clean_review(review):
    # Changing to lowercase
    review = review.lower()
    
    # Changing he'll to he will
    review = re.sub(r"i'm", "i am", review)
    review = re.sub(r"aren't", "are not", review)
    review = re.sub(r"couldn't", "counld not", review)
    review = re.sub(r"didn't", "did not", review)
    review = re.sub(r"doesn't", "does not", review)
    review = re.sub(r"don't", "do not", review)
    review = re.sub(r"hadn't", "had not", review)
    review = re.sub(r"hasn't", "has not", review)
    review = re.sub(r"haven't", "have not", review)
    review = re.sub(r"isn't", "is not", review)
    review = re.sub(r"it't", "had not", review)
    review = re.sub(r"hadn't", "had not", review)
    review = re.sub(r"won't", "will not", review)
    review = re.sub(r"can't", "cannot", review)
    review = re.sub(r"mightn't", "might not", review)
    review = re.sub(r"mustn't", "must not", review)
    review = re.sub(r"needn't", "need not", review)
    review = re.sub(r"shouldn't", "should not", review)
    review = re.sub(r"wasn't", "was not", review)
    review = re.sub(r"weren't", "were not", review)
    review = re.sub(r"won't", "will not", review)
    review = re.sub(r"wouldn't", "would not", review)
    
    review = re.sub(r"\'s", " is", review)
    review = re.sub(r"\'ll", " will", review)
    review = re.sub(r"\'ve", " have", review)
    review = re.sub(r"\'re", " are", review)
    review = re.sub(r"\'d", " would", review)
    
    # Removing links and other stuffs from string
    review = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', review, flags=re.MULTILINE)
    
    review = BeautifulSoup(review, "lxml").text
    
    return review