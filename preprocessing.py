# Importing dependencies
import pickle
import pandas as pd
import numpy as np
from math import ceil
from keras.utils import np_utils

# Importing some constants
from constants import BATCH_SIZE, SEQ_LENGTH, NO_CHARS

# Importing utility method
from utils import clean_review

# Reading the Tokenizer pickle file
with open(r"dataset/tokenizer.pickle", "rb") as input_file:
    tokenizer = pickle.load(input_file)

# Reading the dataset
data = pd.read_csv('dataset/02.tsv', sep='\t', error_bad_lines=False)

print('--There are total {} data samples in the dataset--'.format(len(data)))

# Filtering it
data = data[data['verified_purchase'] == 'Y']

# Selecting reviews with review length > SEQ_LENGTH
data = data[data['review_body'].str.len() > SEQ_LENGTH]

# Selecting review_body column
data = data[['review_body']]

# Dropping empty rows
data = data.dropna()

# Shuffling the data
data = data.sample(frac=1)

# Selecting first 6000 samples
data = data.head(BATCH_SIZE * 2)

print('--After cleaning, there are total {} data samples in the dataset--'.format(len(data)))

# Spliting the data into batches
for i in range(ceil(len(data) / BATCH_SIZE)):
    # Selecting a part of the data
    batch = data.iloc[i * BATCH_SIZE: (i*BATCH_SIZE) + BATCH_SIZE].values
    
    review_seq = []
    nxt_seq = []
    
    # Iterating through the reviews
    for index, review in enumerate(batch):
        if index % 1000 == 0:
            print('--Preprocessing batch {} review {}--'.format(i+1, index+1))
        
        # Cleaning the reviews
        review = clean_review(review[0])
        
        # Generating the sequences
        for k in range(len(review) - SEQ_LENGTH):
            # Seleting the sequence
            seq = review[k:SEQ_LENGTH + k]
            nxt = review[SEQ_LENGTH + k]
            
            # Using tokenizer to convert the review into vector
            seq = tokenizer.texts_to_sequences(seq)
            nxt = tokenizer.texts_to_sequences(nxt)
            
            seq_vec = []
            nxt_vec = []
            
            for char in seq:
                if len(char) == 1:
                    seq_vec.append(char[0])
                else:
                    seq_vec.append(0)
                    
            for char in nxt:
                if len(char) == 1:
                    nxt_vec.append(char[0])
                else:
                    nxt_vec.append(0)       
            
            # Using One Hot 
            seq_one_hot = np_utils.to_categorical(seq_vec, NO_CHARS + 1)
            nxt_one_hot = np_utils.to_categorical(nxt_vec, NO_CHARS + 1)
            
            review_seq.append(seq_one_hot)
            nxt_seq.append(nxt_one_hot[0])

    sequence_arr = np.array(review_seq)
    next_arr = np.array(nxt_seq)
    
    print('--Generated {}sequences--'.format(len(sequence_arr)))
    
    # Saving the dataset
    np.save('dataset/sequence_review_{}'.format(i), sequence_arr)
    np.save('dataset/next_review_{}'.format(i), next_arr)