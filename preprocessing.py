import pandas as pd

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

