import numpy as np
from sklearn.model_selection import train_test_split
from keras.layers import Dense, LSTM, CuDNNLSTM
from keras.models import Sequential
from keras import optimizers
from keras.callbacks import EarlyStopping, ModelCheckpoint

nxt = np.load('./dataset/next_review_0.npy')
seq = np.load('./dataset/sequence_review_0.npy')

X_train, X_test, y_train, y_test = train_test_split(seq, nxt, test_size=0.1, random_state=1969)

del nxt, seq

model = Sequential()

model.add(CuDNNLSTM(128, input_shape=(40, 51)))
model.add(Dense(64, activation='relu'))
model.add(Dense(51, activation='softmax'))

# Compiling the model
model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=0.01), metrics=['accuracy'])

# Printing the model summary
print(model.summary())

# Added early stopping system to monitor validation loss on each epoch and stops training when validation loss start to increase
monitor = EarlyStopping(monitor='val_loss', 
                        patience=5, 
                        mode='min',
                        restore_best_weights=True)

# Saving the model in every epochs for some experiments
checkpoint = ModelCheckpoint(filepath="model.{epoch:02d}-{val_loss:.2f}.h5")

# Starting the training process
model.fit(X_train, 
          y_train, 
          validation_data=(X_test, y_test), 
          epochs=500, 
          batch_size=3000, 
          callbacks=[monitor, checkpoint])