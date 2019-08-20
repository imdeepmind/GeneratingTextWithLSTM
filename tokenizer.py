# Importing dependencies
import pickle
import pandas as pd
from keras.preprocessing.text import Tokenizer

# Importing itility method clean_review
from utils import clean_review

# Importing constants
from constants import NO_CHARS

# Initializing tokenizer
tokenizer = Tokenizer(num_words=NO_CHARS, filters='')

# Reading data
data = pd.read_csv('dataset/02.tsv', sep='\t', error_bad_lines=False)

# Filtering data
data = data[data['verified_purchase'] == 'Y']

# We need the review_body column
data = data[['review_body']]

# Dropping empty rows
data = data.dropna()

# Converting dataframe to numpy array
data = data.values

# Iterating through reviews
for index, review in enumerate(data):
    if index % 1000 == 0:
        print('Tokenizing review {}'.format(index))
    
    # Cleaning reviews
    review = clean_review(review[0])
    
    # Fitting the texts on tokenizer
    tokenizer.fit_on_texts(review)

# Saving the tokenizer as pickle
with open('dataset/tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)