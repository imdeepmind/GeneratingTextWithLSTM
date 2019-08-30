from keras.models import Sequential
from keras.layers import Dense, LSTM, CuDNNLSTM
from keras import optimizers

from generator import DataGenerator
from constants import DATABASE, BATCH_SIZE, MAX_LENGTH, NO_ROWS_TRAIN, NO_ROWS_VAL, GPU

dataGenerator = DataGenerator(DATABASE, BATCH_SIZE, MAX_LENGTH)

trainGenerator = dataGenerator.trainGenerator()
valGenerator = dataGenerator.validationGenerator()

model = Sequential()

if GPU:
    model.add(CuDNNLSTM(128, input_shape=(MAX_LENGTH, 128)))
else:
    model.add(LSTM(128, input_shape=(MAX_LENGTH, 128)))
model.add(Dense(128, activation='softmax'))

optimizer = optimizers.RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

model.fit_generator(trainGenerator, 
                    epochs=10, 
                    steps_per_epoch=NO_ROWS_TRAIN // BATCH_SIZE,
                    validation_data=valGenerator,
                    validation_steps=NO_ROWS_VAL // BATCH_SIZE)