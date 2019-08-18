import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM, CuDNNLSTM
from keras import optimizers
from keras.layers.embeddings import Embedding
from keras.callbacks import EarlyStopping, ModelCheckpoint
from utils import CHARS

# Loading the data
data = np.load('dataset/sequence.npy')

# For testing, im using a fraction of the data
#data = data[0: 1000000]

# Some constants
GPU = False
SEQ_LENGTH = 40
VOCAB_SIZE = len(CHARS) + 1
EPOCHS = 50
BATCH_SIZE = 1024

# Dividing the dataset
X = data[:, 0: SEQ_LENGTH]
y = pd.get_dummies(data[:, SEQ_LENGTH]).values

del data

# Spliting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1969)

del X, y

# Making the suquentual model
model = Sequential()
model.add(Embedding(VOCAB_SIZE, 128, input_length=SEQ_LENGTH))

if GPU:
  model.add(CuDNNLSTM(128))
else:
  model.add(LSTM(128))
  
model.add(Dense(64, activation='relu'))
model.add(Dense(y_train.shape[1], activation='softmax'))

# Compiling the model
model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=0.01), metrics=['accuracy'])

# Printing the model summmary
print(model.summary())

# Added early stopping system to monnitor validation loss on each epoch and stops training when validation loss start to increase
monitor = EarlyStopping(monitor='val_loss', 
                        patience=5, 
                        mode='min',
                        restore_best_weights=True)

# Saving the model in every epochs for some experiments
checkpoint = ModelCheckpoint(filepath="weights/model.{epoch:02d}-{val_loss:.2f}.h5")

# Starting the training process
model.fit(X_train, 
          y_train, 
          validation_data=(X_test, y_test), 
          epochs=EPOCHS, 
          batch_size=BATCH_SIZE, 
          callbacks=[monitor, checkpoint])

# Saving the model
model.save('weights/model_best.h5')