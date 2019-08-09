import pandas as pd

from utils import clean_review, character_to_ascii

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
data = data.sample(frac=0.2)

data = data.values

review_sequence = []
review_next = []

for index, review in enumerate(data):
    if index % 1000 == 0:
        print('--Processing {}th review'.format(index))
    
    review = review[0]
    
    # Cleaning the reviews
    review = clean_review(review)
    
    for i in range(len(review) - SEQ_LENGTH):
        seq = review[i:SEQ_LENGTH + i]
        nxt = review[SEQ_LENGTH + i]
        
        seq = character_to_ascii(seq)
        nxt = character_to_ascii(nxt)[0]
        
        review_sequence.append(seq)
        review_next.append(nxt)
    