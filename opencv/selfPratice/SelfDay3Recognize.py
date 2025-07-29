import cv2 as cv
import numpy as np 
import pyttsx3

# Load the trained model
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("trained_model.yml")

# Load label-to-name mapping
label_to_name = {}
with open("labels.txt", "r") as f:
    for line in f:
        label, name = line.strip().split(":")
        label_to_name[int(label)] = name


# setup text-to speech
engine = pyttsx3.init()

# Track who is already greeted 
greeted_people = set()

# Load face detector 
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# start a webcam
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect Faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for(x,y,w,h) in faces:
        # Draw Rectangle
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

        # Resize the face and recognize
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv.resize(roi_gray, (200,200))

        # predict
        label, confidence = recognizer.predict(roi_gray)

        # set label text
        name = label_to_name.get(label, "Unknown")

        if name != "Unknown" and name not in greeted_people:
            greeted_people.add(name)
            print(f" Hello {name}")
            engine.say(f"Hello {name}")
            engine.runAndWait()
        
        

        # Show name and confidence
        cv.putText(frame, name, (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0),2)

    
    # Display
    cv.imshow("Face Recognition", frame)

    if cv.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv.destroyAllWindows()