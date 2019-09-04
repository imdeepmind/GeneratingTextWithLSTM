# Importing dependencies
from keras.models import Sequential
from keras.layers import Dense, LSTM, CuDNNLSTM
from keras.layers.embeddings import Embedding
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras import optimizers
import os

# importing my generator
from generator import DataGenerator
from callback import CustomCallback

# Importing constants
from constants import DATABASE, BATCH_SIZE, MAX_LENGTH,  NO_ROWS_TRAIN, NO_ROWS_VAL, GPU, WEIGHT_FOLDER, EPOCHS, OUTPUT_CLASSES, ONE_HOT_MODE, VOCAB_SIZE

# Creating weights folder if it isn't exists
if not os.path.exists(WEIGHT_FOLDER):
    os.makedirs(WEIGHT_FOLDER)

# Initializing generator
dataGenerator = DataGenerator(DATABASE, BATCH_SIZE, MAX_LENGTH, ONE_HOT_MODE)

# Making the generation functions for train and val
trainGenerator = dataGenerator.trainGenerator()
valGenerator = dataGenerator.validationGenerator()

# Keras sequencial model
model = Sequential()

model.add(Embedding(VOCAB_SIZE, 128, input_length=MAX_LENGTH))

# If GPU then using CuDNNLSTM else using LSTM
print(GPU)
if GPU:
    model.add(CuDNNLSTM(128))
else:
    model.add(LSTM(128))

# Output layer
model.add(Dense(OUTPUT_CLASSES, activation='softmax'))

# Compiling the model and initializng optimizer
optimizer = optimizers.RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Using early stopping for controlling the epochs
monitor = EarlyStopping(monitor='val_loss', 
                        patience=5, 
                        mode='min',
                        restore_best_weights=True)

# Saving the model in every epochs for some experiments
checkpoint = ModelCheckpoint(filepath=WEIGHT_FOLDER + "/model.{epoch:02d}-{val_loss:.2f}.h5")

# Custom callback for generating samples 
predictChars = CustomCallback()

# Training the model
model.fit_generator(trainGenerator, 
                    epochs=EPOCHS, 
                    steps_per_epoch=NO_ROWS_TRAIN // BATCH_SIZE,
                    validation_data=valGenerator,
                    validation_steps=NO_ROWS_VAL // BATCH_SIZE,
                    callbacks=[monitor, checkpoint])

# Saving the model
model.save("{}/model.best.h5".format(WEIGHT_FOLDER))