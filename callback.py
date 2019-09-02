# Importing dependencies
import keras
import numpy as np

# Importing some constants
from constants import DEMO_REVIEW, PREDICT_CHARS, MAX_LENGTH

# Class CustomCallback 
class CustomCallback(keras.callbacks.Callback):
    # This method intriduces some randomness in the prediction
    def sample(self, preds, temperature=1.0):
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)
        return np.argmax(probas)
    
    # This method is used to one hot all inputs
    def one_hot(self, seq):
        # Initializng a zero matrxi
        x = np.zeros((1, MAX_LENGTH, 128), dtype=np.bool)
        
        # Iterating through the seq to generate one hot
        for i, sentence in enumerate([seq]):
            for t, char in enumerate(sentence):
                x[i, t, char] = 1
        
        # Returning the x
        return x
    
    # This method runs after each epoch
    def on_epoch_end(self, epoch, logs={}):
        # Selecting first 40 characters and also converting the text into lowercase as the model supports it only
        review = DEMO_REVIEW.lower()[0:MAX_LENGTH]
        review = [ord(i) for i in review]
        
        # Predicting the next characters for PREDICT_CHARS times
        for k in range(PREDICT_CHARS):
            # Here im selecting the first 40 characters and using the one hot method to encode the data
            x = self.one_hot(review[k: k + MAX_LENGTH])
            
            # Predicting using the model
            temp = self.model.predict(x)
            
            # Calling the sample method
            temp = self.sample(temp[0])
            
            # Appending the predicted charcter
            review.append(temp)
        
        # Printing some info and predicted text
        print('Currently at epoch {}'.format(epoch))
        print('Starter text : {}'.format(DEMO_REVIEW))
        print('Generated text: {}'.format(''.join([chr(i) for i in review])))