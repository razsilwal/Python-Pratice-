import cv2 as cv

# read the image

img = cv.imread(r"opencv\images\WIN_20230422_12_18_13_Pro.jpg")

resize = cv.resize(img, (600,600))
gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

# Haar cascade

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

for(x,y,w,h) in faces:
    cv.rectangle(resize, (x,y), (x+w , y+h), (0,255,0), 2)

cv.imshow("Faces", resize)
cv.waitKey(0)