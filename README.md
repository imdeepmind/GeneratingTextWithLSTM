# Generating Text with LSTM Recurrent Neural Networks

The aim of this project is to generate text using LSTM Recurrent Neural Networks. LSTM Recurrent Neural Networks are powerful Deep Learning models that are used for learning sequenced data. Here an LSTM model is trained on 200 million samples, and the idea is that after training on 200 million samples, it should be able to generate text. 

## Table of contents:
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Model](#model)
- [Dependencies](#dependencies)
- [File Structure](#file-structure)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)

## Introduction

TODO


## Dataset

For this project, I'm using the [Amazon Review Dataset](https://s3.amazonaws.com/amazon-reviews-pds/readme.html). Amazon Review Dataset is a gigantic collection of product reviews. It contains more than 130 millions of reviews. In this project, I have used a small fraction of the original dataset.

> Downloading instructions and other information about the dataset can be found on the dataset website.

After that, the dataset is preprocessed so that it can be used here in this project. During preprocessing, first, the dataset is cleaned and then divided into sequences. After that, the preprocessed dataset contains a sequence of characters and the next character. Here the model is trained to predict the next character based on the sequence of characters.

To know more about the preprocessing step, please check this [GitHub repositiry](https://github.com/imdeepmind/AmazonReview-LanguageGenerationDataset). Also to down the dataset please click [here](https://www.kaggle.com/imdeepmind/language-generation-dataset-200m-samples/).

## Model

TODO

## Dependencies

The project is developed using Python 3.6. Further, some other libraries are also used. Below is a list of the libraries used in this project.
-	Keras==2.2.4
-	Numpy==1.16.2
-	Pandas==0.24.2
-	Sqlite3==2.6.0

## File Structure

TODO

## Future Improvements

TODO

## Acknowledgments
- [Amazon Review Dataset](https://s3.amazonaws.com/amazon-reviews-pds/readme.html)
- ["Text Generation With LSTM Recurrent Neural Networks in Python with Keras" blog by machinelearningmastery.com](https://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/)
- [Keras code example of LSTM for text generation by keras-team](https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py)
