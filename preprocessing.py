import pandas as pd
import numpy as np
from imblearn.under_sampling import RandomUnderSampler

from utils import clean_review, character_to_number, CHARS

# Constants
SEQ_LENGTH = 40

randomSampler = RandomUnderSampler(random_state=1969)

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

# As I have limited RAM(8GB), I'll only work with fraction of the data
data = data.sample(frac=0.05)

data = data.values

review_df = pd.DataFrame(columns=['sequence', 'next'])
review_sequence = []
next_sequence = []

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
        
        # Appending the data
        review_sequence.append(seq)
        next_sequence.append(nxt)

del data

review_df['sequence'] = review_sequence
review_df['next'] = next_sequence

del review_sequence, next_sequence

review_df = review_df[review_df['next'] != CHARS['--']]

review_df = review_df.sample(frac=1)

X, y = randomSampler.fit_resample(review_df['sequence'].values.reshape(-1,1),review_df['next'].values.reshape(-1,1))

del review_df

final_data = []

for i in range(len(X)):
    temp = X[i][0]
    temp.append(y[i][0])
    final_data.append(temp)

# Converting the array into numpy array
dataset = np.array([final_data])

del final_data

# Reshaping the data
dataset = dataset.reshape(dataset.shape[1], SEQ_LENGTH + 1)

# Saving the numpy array
np.save('dataset/sequence', dataset)