def pred():
	import numpy as np
	import tensorflow as tf
	import json
	import cv2

	IMG_WIDTH = 50
	IMG_HEIGHT = 50

	model = tf.keras.models.load_model('assets')
	image = cv2.imread('image.png', cv2.IMREAD_UNCHANGED)
	cv2.imwrite('image.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
	image = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
	# print(image.shape)

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

if __name__ == '__main__':
	pred()
