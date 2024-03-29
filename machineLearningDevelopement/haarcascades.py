# -*- coding: utf-8 -*-
"""haarCascades.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J-opZIyr0YtVDKCHvxe2UgqSbq2h4Enh
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
# ! kaggle datasets download -d jangedoo/utkface-new
# ! mkdir ageData2
# ! unzip utkface-new.zip -d ageData2

import cv2
import numpy as np
import os 
from google.colab.patches import cv2_imshow

anotherPath = "/content/drive/MyDrive/haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(anotherPath)

type(face_cascade)

path = "/content/ageData1/face_age/030/1773.png"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
count=0
print(faces)
for (x,y,w,h) in faces:
  count += 1
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2_imshow(img)
print(count)

cv2.COLOR_BGR2GRAY

augmentedFolder = "/content/drive/MyDrive/ComputingNea"

import time
import os
lst = list(os.listdir(augmentedFolder))
# for folder in os.listdir(augmentedFolder):
#   lst.append(folder)
  # time.sleep(0.5)

for i in lst:
  print(i)
  time.sleep(0.5)

len(lst)

