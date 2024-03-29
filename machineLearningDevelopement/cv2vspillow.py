# -*- coding: utf-8 -*-
"""cv2VsPillow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kui0Cj6eiROsyWXCS0f5EyRHRaarFzXq
"""

! pip install -q kaggle
from google.colab import files
files.upload()
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json
import kaggle
! kaggle datasets download -d frabbisw/facial-age
! mkdir ageData1
from google.colab import output
! unzip facial-age.zip -d ageData1
! kaggle datasets download -d jangedoo/utkface-new
! mkdir ageData2
! unzip utkface-new.zip -d ageData2
output.clear()

import math
import numpy as np
import os
import sys
import tensorflow as tf
from PIL import Image, features
from tqdm import tqdm
from google.colab import files, output
from google.colab.patches import cv2_imshow
import cv2

categories = [[1,17],
              [18,1000]]

data_dir1 = "/content/ageData1/face_age"
data_dir2 = "/content/ageData2/UTKFace"
EPOCHS = 10
IMG_WIDTH = 200
IMG_HEIGHT = 200
NUM_CATEGORIES = len(categories)
TEST_SIZE = 0.1
images = []
labels = []
file_name_counter = 0

augmentedFolder = "/content/drive/MyDrive/ComputingNea"

'''
takes in data from the UTK face dataset
'''
another_useless_array = []
for randomFile in tqdm(os.listdir(data_dir2)):
  folder_path = os.path.join(data_dir2, randomFile)
  var = randomFile[:3]
  if not var.isdigit():
    var = randomFile[:2]
    if not var.isdigit():
      var = randomFile[:1]

  counter = 0 
  while counter < len(categories):
    if categories[counter][0] <= int(var) <= categories[counter][1]:
      temp = counter
      break
    counter += 1

  try:
    
    image = cv2.imread(folder_path, cv2.IMREAD_COLOR)
    
    for i in range(-20, 21, 5):
      
      file_name_counter += 1

      height, width = image.shape[:2]
      center = (width/2, height/2)
      newImage = cv2.warpAffine(src=image, M= cv2.getRotationMatrix2D(center=center, angle=i, scale=1) , dsize=(width, height))
      
      newImage = cv2.resize(newImage, (IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_LINEAR)
      newTemp = f'{temp}_{i}_{file_name_counter}.jpg'
      
      cv2.imwrite(os.path.join(augmentedFolder, newTemp), newImage)
  
  except Exception as e:
    another_useless_array.append(randomFile)
    print(e)
    pass


print(set(another_useless_array))
# output.clear()

len(os.listdir(augmentedFolder))

