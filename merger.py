import numpy as np
import os 

files = os.listdir('dataset/')

files.remove('02.tsv')

if 'sequence.npy' in files:
    files.remove('sequence.npy')

data = np.load('dataset/' + files[0])

del files[0]

for file in files:
    print('--Merging file {}--'.format(file))
    temp = np.load('dataset/' + file)
    
    data = np.concatenate((data, temp))

np.save('dataset/sequence', data)