import pandas as pd
import numpy as np

from utils import clean_review, character_to_number

# Constants
SEQ_LENGTH = 40

# Reading data
data = pd.read_csv('dataset/02.tsv', sep='\t', error_bad_lines=False)

# Filtering data
data = data[data['verified_purchase'] == 'Y']

# Converting data type of columns review_body
data = data.astype({'review_body' : 'str'})

# Selecting reviews with review length > SEQ_LENGTH
data = data[data['review_body'].str.len() > SEQ_LENGTH]
        
# Selecting the two columns
data = data[['review_body']]

# Dropping rows with nan values
data = data.dropna()

# As I have limited RAM(8GB), I'll only work with 
data = data.sample(frac=0.05)

data = data.values

review_sequence = []

for index, review in enumerate(data):
    if index % 1000 == 0:
        print('--Processing {}th review'.format(index))
    
    review = review[0]
    
    # Cleaning the reviews
    review = clean_review(review)
    
    # Generating sequence
    for i in range(len(review) - SEQ_LENGTH):
        # Selecting the sequence
        seq = review[i:SEQ_LENGTH + i]
        nxt = review[SEQ_LENGTH + i]
        
        # Converting to ascii
        seq = character_to_number(seq)
        nxt = character_to_number(nxt)[0]
        
        seq.append(nxt)
        
        # Appending the data
        review_sequence.append(seq)

del data

# Converting the array into numpy array
dataset = np.array([review_sequence])

del review_sequence

# Reshaping the data
dataset = dataset.reshape(dataset.shape[1], SEQ_LENGTH + 1)

# Saving the numpy array
np.save('dataset/sequence', dataset)