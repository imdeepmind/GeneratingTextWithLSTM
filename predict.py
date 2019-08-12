from keras.models import load_model
from keras import optimizers
from utils import clean_review, character_to_number, number_to_character, get_character_from_index
import numpy as np

SEQ_LENGTH = 40
PREDICT_CHRS = 100

# Loading the model
model = load_model('weights/model_best.h5')

# Compiling the model
model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=0.01), metrics=['accuracy'])

start = ''
while len(clean_review(start)) <= SEQ_LENGTH:
    start = input('Please enter 40 charcters for the review: ')

start = clean_review(start)

start = start[0:SEQ_LENGTH]

print('You typed: ' + start)

start = character_to_number(start)

review = start

for i in range(PREDICT_CHRS):
    temp = model.predict_classes(np.array([start]))[0]
    start = np.hstack([start, temp])
    review = np.hstack([review, temp])
    start = np.delete(start, 0,0)
    
print('Generated Review: ' + number_to_character(review))
