import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def returnFaceList(image_path):
	img = cv2.imread(image_path)
	height, width, channels = img.shape
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	return faces

def FacialMean(Correct_Path):
	numbers = []
	for image in os.listdir(Correct_Path):
		try:
			faces = returnFaceList(Correct_Path+'/'+image)
			facial_area = faces[0][2] * faces[0][3]
			image_area = height * width
			proportion = (facial_area/image_area) * 100
			numbers.append(proportion)
		except:
			print ("Leaving out: " + image)
	print (sum(numbers)/len(numbers))

def detectNumberOfFaces(filename):
	faces = returnFaceList(filename)
	facial_area = faces[0][2] * faces[0][3]
	image_area = height * width
	proportion = (facial_area/image_area) * 100
	if len(faces) > 1:
	    print ("Many Faces")

	elif int(proportion) >= 20:
	    print ("Correct proportion")

	else:
	    print ("Skewed")

def drawFaces(filename):
	faces = returnFaceList(filename)
	for (x,y,w,h) in faces:
	    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]  

	cv2.imshow('img',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

drawFaces("./Correct/200061.jpeg")