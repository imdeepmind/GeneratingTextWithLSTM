import numpy as np

print('--Reading file--')
sequence_data1 = np.load('dataset/sequence_review_0.npy')
sequence_data2 = np.load('dataset/sequence_review_1.npy')

print('--Merging data--')
data = np.concatenate((sequence_data1, sequence_data2))

del sequence_data2, sequence_data1

np.save('dataset/sequence', data)

del data

print('--Reading file--')
next_data1 = np.load('dataset/next_review_0.npy')
next_data2 = np.load('dataset/next_review_1.npy')

print('--Merging data--')
data = np.concatenate((next_data1, next_data2))

del next_data2, next_data1

np.save('dataset/next', data)

del data