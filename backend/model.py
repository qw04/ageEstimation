def pred():
	import numpy as np
	import tensorflow as tf
	import json
	import cv2


	a_file = open("file.json", "r")
	json_object = json.load(a_file)
	a_file.close()

	if json_object["boundary"] == "21":
		model = tf.keras.models.load_model('twenty_one')
	elif json_object["boundary"] == "18":
		model = tf.keras.models.load_model('eighteen')

	IMG_WIDTH = 50
	IMG_HEIGHT = 50

	image = cv2.imread('image.png', cv2.IMREAD_UNCHANGED)
	cv2.imwrite('image.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
	image = cv2.imread('image.jpg', cv2.IMREAD_COLOR)

	anotherPath = "haarcascade_frontalface_default.xml"
	face_cascade = cv2.CascadeClassifier(anotherPath)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 3)
	# print(len(faces))

	if len(faces) == 1:

		image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_AREA)
		predictions = model.predict(np.array([image]))
		predictions = predictions.tolist()[0]
		# print(predictions)

		a_file = open("file.json", "r")
		json_object = json.load(a_file)
		a_file.close()

		a_file = open("file.json", "w")
		json_object["a"] = predictions.index(max(list(predictions)))
		json.dump(json_object, a_file)
		a_file.close()

	elif len(faces) == 0:

		a_file = open("file.json", "r")
		json_object = json.load(a_file)
		a_file.close()

		a_file = open("file.json", "w")
		json_object["a"] = "no faces"
		json.dump(json_object, a_file)
		a_file.close()		

	elif len(faces) >= 2:
		
		a_file = open("file.json", "r")
		json_object = json.load(a_file)
		a_file.close()

		a_file = open("file.json", "w")
		json_object["a"] = "too many faces"
		json.dump(json_object, a_file)
		a_file.close()

if __name__ == '__main__':
	pred()
