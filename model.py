import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM
from keras import optimizers
from keras.layers.embeddings import Embedding

data = np.load('dataset/sequence.npy')

X = data[:, 0: 40]
y = pd.get_dummies(data[:, 40]).values

del data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1969)

del X, y

model = Sequential()
model.add(Embedding(128, 128, input_length=40))
model.add(LSTM(128))
model.add(Dense(64, activation='relu'))
model.add(Dense(y_train.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=0.01), metrics=['accuracy'])

print(model.summary())

model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32)