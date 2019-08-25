from keras.models import Sequential
from keras.layers import Dense, LSTM, CuDNNLSTM
from keras import optimizers

from generator import DataGenerator
from constants import DATABASE, BATCH_SIZE, MAX_LENGTH, NO_ROWS, GPU

dataGenerator = DataGenerator(DATABASE, BATCH_SIZE, MAX_LENGTH)
generator = dataGenerator.generator()

model = Sequential()

if GPU:
    model.add(CuDNNLSTM(128, input_shape=(MAX_LENGTH, 128)))
else:
    model.add(LSTM(128, input_shape=(MAX_LENGTH, 128)))
model.add(Dense(128, activation='softmax'))

optimizer = optimizers.RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

model.fit_generator(generator, epochs=10, steps_per_epoch=NO_ROWS // BATCH_SIZE)