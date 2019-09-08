

# Generating Text with LSTM Recurrent Neural Networks

The aim of this project is to generate text using LSTM Recurrent Neural Networks. LSTM Recurrent Neural Networks are powerful Deep Learning models that are used for learning sequenced data. Here an LSTM model is trained on 200 million samples, and the idea is that after training on 200 million samples, it should be able to generate text. 

## Table of contents:
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model](#model)
- [Sample Results](#sample-results)
- [Dependencies](#dependencies)
- [File Structure](#file-structure)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)

## Introduction

Recurrent Neural Networks are great in learning sequenced data. With enough data and computational power, they can learn very complex things. 

In this project LSTM Recurrent Neural Networks are used to generating text. 

To do that, the model is trained on the dataset of text characters. The dataset contains 40 character long sequences and the next character after the sequence. The model is here predicting the next character based on the 40 characters long sequence.  


## Dataset

For this project, I'm using the [Amazon Review Dataset](https://s3.amazonaws.com/amazon-reviews-pds/readme.html). Amazon Review Dataset is a gigantic collection of product reviews. It contains more than 130 millions of reviews. In this project, I have used a small fraction of the original dataset.

> Downloading instructions and other information about the dataset can be found on the dataset website.

After that, the dataset is preprocessed so that it can be used here in this project. During preprocessing, first, the dataset is cleaned and then divided into sequences. After that, the preprocessed dataset contains a sequence of characters and the next character. Here the model is trained to predict the next character based on the sequence of characters.

To know more about the preprocessing step, please check this [GitHub repositiry](https://github.com/imdeepmind/AmazonReview-LanguageGenerationDataset). Also to download the dataset please click [here](https://www.kaggle.com/imdeepmind/language-generation-dataset-200m-samples/).

## Model

Generating text is not an easy task for a computer, it is one of the hardest problem for computers. Here, in this project, to solve this problem, different types of Networks were used.

The first layer in the model is a [Embedding](https://keras.io/layers/embeddings/) layer. In Keras, an Embedding layer is a work embedding layer (word2vec or glove). This layer is used to generate a vector representation of each sequence in our training sample. 

The send layer is an LSTM layer. LSTM of Long Short Term Memory Recurrent Neural Network is a type of Neural Network, that is used for sequenced data. 

> Here is a [link](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) to a great blog on LSTM.  If you want to learn more about LSTM, please read it.

The third layer is a Dense layer with ReLu activation method. In Keras, Dense is a normal densely connected Neural Network. And then, we have a Dropout layer, just to prevent overfitting.

Finally, the output Softmax layer for predicting the outputs.


## Sample Results

TODO

## Dependencies

The project is developed using Python 3.6. Further, some other libraries are also used. Below is a list of the libraries used in this project.
-	Keras==2.2.4
-	Numpy==1.16.2
-	Pandas==0.24.2
-	Sqlite3==2.6.0

## File Structure

Following are the files in the project.
- callback.py - This class is used for generating some samples results after each epoch
- constants.py - This file contains all the constants for the project
- generator.py - This file contains a generator that is used to read the data in a batch
- model.py - This file contains the main model for the project
- predict.py - This is a simple script for predicting some text using the trained model

## Future Improvements

Currently, the model is trained only on 30 million samples, not 200 million samples due to technical limitation. If the model is trained on 200 million samples, then the model can perform better.

## Acknowledgments
- [Amazon Review Dataset](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)
- [Text Generation With LSTM Recurrent Neural Networks in Python with Keras blog by machinelearningmastery.com](https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/)
- [Keras code example of LSTM for text generation by keras-team](https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py)
