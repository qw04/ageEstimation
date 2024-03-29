# -*- coding: utf-8 -*-
"""tryingOutNonCategoricalLabels.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p310npmr1CJU1NG1F-Btd-4IeCurWCnq
"""

! pip install -q kaggle
from google.colab import files
files.upload()
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json
! kaggle datasets list
import kaggle
! kaggle datasets download -d frabbisw/facial-age
! mkdir ageData1
! unzip facial-age.zip -d ageData1
! kaggle datasets download -d jangedoo/utkface-new
! mkdir ageData2
! unzip utkface-new.zip -d ageData2

import math
import cv2
import numpy as np
import os
import sys
import tensorflow as tf
from sklearn.model_selection import train_test_split

data_dir1 = "/content/ageData1/face_age"
data_dir2 = "/content/ageData2/UTKFace"
EPOCHS = 20
IMG_WIDTH = 50
IMG_HEIGHT = 50
NUM_CATEGORIES = 1
TEST_SIZE = 0.3
images = []
labels = []

another_useless_array = []
for folder in os.listdir(data_dir1):
  folder_path = os.path.join(data_dir1, folder)
  if os.path.isdir(folder_path) and folder != 'face_age':
    temp = int(folder)
    for file in os.listdir(folder_path):
      try:
        if folder != 'face_age':
          image = cv2.imread(os.path.join(folder_path, file), cv2.IMREAD_COLOR)
          image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_AREA)
          images.append(image)
          labels.append(temp)
      except Exception as e:
        print(e)
        another_useless_array.append(folder)
        pass
another_useless_set = set(another_useless_array)
print(another_useless_set)
#print(image[0])

for randomFile in os.listdir(data_dir2):
  folder_path = os.path.join(data_dir2, randomFile)
  var = randomFile[:2]
  if not var.isdigit():
    var = var[0]
  temp = int(var)
  try:  
    image = cv2.imread(folder_path, cv2.IMREAD_COLOR)
    image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_AREA)
    images.append(image)
    labels.append(temp)
  except Exception as e:
    another_useless_array.append(randomFile)
    pass
print(set(another_useless_array))

labels = [x/110 for x in labels]

min(labels)

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation="sigmoid", input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        tf.keras.layers.MaxPooling2D(pool_size=(3, 3)),
        tf.keras.layers.Conv2D(32, (3, 3), activation="sigmoid"),
        tf.keras.layers.MaxPooling2D(pool_size=(3, 3)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(NUM_CATEGORIES * 64, activation="sigmoid"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(NUM_CATEGORIES * 32, activation="sigmoid"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(NUM_CATEGORIES * 16, activation="sigmoid"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(NUM_CATEGORIES * 8, activation="sigmoid"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(NUM_CATEGORIES * 4, activation="sigmoid"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(NUM_CATEGORIES * 2, activation="sigmoid"),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model

model = get_model()
# model.summary()

x_train, x_test, y_train, y_test = train_test_split(
    np.array(images), np.array(labels), test_size=TEST_SIZE
    )

model.fit(x_train, y_train,
          epochs=EPOCHS,
          )

predictions = model.predict(x_test)
predictions = predictions.tolist()

predictions = [x[0]*110 for x in predictions]

set(predictions)

correct = 0
incorrect = 0
for i, j in zip(predictions, y_test):
  if j > 20:
    tempTest = 1
  else:
    tempTest = 0
  if i > 20:
    tempPrediction = 1
  else:
    tempPrediction = 0
  if tempPrediction == tempTest:
    correct += 1
  else:
    incorrect += 1
accuracy = (correct)/(correct+incorrect)
print(f'accuracy: {accuracy}')

print(set(predictions))

print(y_test[:5])

print(predictions[:5])

