import pickle
import pandas as pd
from keras.preprocessing.text import Tokenizer

from constants import NO_CHARS
from utils import clean_review

tokenizer = Tokenizer(num_words=NO_CHARS, filters='')

data = pd.read_csv('dataset/02.tsv', sep='\t', error_bad_lines=False)

data = data[data['verified_purchase'] == 'Y']

data = data[['review_body']]

data = data.dropna()

data = data.values

for index, review in enumerate(data):
    if index % 1000 == 0:
        print('Tokenizing review {}'.format(index))
        
    review = clean_review(review[0])
    
    tokenizer.fit_on_texts(review)
    
with open('dataset/tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)