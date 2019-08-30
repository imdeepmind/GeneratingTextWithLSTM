import keras
import numpy as np

from constants import DEMO_REVIEW, PREDICT_CHARS, MAX_LENGTH

class CustomCallback(keras.callbacks.Callback):
    def one_hot(self, seq):
        x = np.zeros((1, MAX_LENGTH, 128), dtype=np.bool)
        
        for i, sentence in enumerate([seq]):
            for t, char in enumerate(sentence):
                x[i, t, char] = 1
        
        return x
    
    def on_epoch_end(self, epoch, logs={}):
        review = DEMO_REVIEW.lower()[0:MAX_LENGTH]
        review = [ord(i) for i in review]
        
        for k in range(PREDICT_CHARS):
            x = self.one_hot(review[k: k + MAX_LENGTH])
            
            temp = self.model.predict_classes(x)
            review.append(temp[0])
        
        print('Currently at epoch {}'.format(epoch))
        print('Starter text : {}'.format(DEMO_REVIEW))
        print('Generated text: {}'.format(''.join([chr(i) for i in review])))