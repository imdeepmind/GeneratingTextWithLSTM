# Importing dependencies
import keras
import numpy as np

# Importing some constants
from constants import DEMO_REVIEW, PREDICT_CHARS, MAX_LENGTH, TEMPERATURE

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
    
    # This method runs after each epoch
    def on_epoch_end(self, epoch, logs={}):
        # Printing some info and predicted text
        print('Currently at epoch {}'.format(epoch + 1))
        print('Starter text : {}'.format(DEMO_REVIEW))
        
        for temperature in TEMPERATURE:
            # Selecting first 40 characters and also converting the text into lowercase as the model supports it only
            review = DEMO_REVIEW.lower()[0:MAX_LENGTH]
            review = [ord(i) for i in review]
            
            # Predicting the next characters for PREDICT_CHARS times
            for k in range(PREDICT_CHARS):  
                # Predicting using the model
                temp = self.model.predict(np.array([review[k: k + MAX_LENGTH]]))

                # Calling the sample method
                temp = self.sample(temp[0], temperature)

                # Appending the predicted charcter
                review.append(temp)
        

            print('Generated text with temperature {}: {}'.format(temperature, ''.join([chr(i) for i in review])))