# ------------------------- #
# Face Recogination #
# ------------------------- #


# Step 1 Collect face images and label them

import cv2 as cv 
import os
import numpy as np 


# # Load the face detection model
# face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Ask the user for the person name 
# person_name = input("Enter the name of the person")

# # Create folder if not exists
# dataset_path = "saved_faces"
# person_path = os.path.join(dataset_path, person_name)
# os.makedirs(person_path, exist_ok=True)

# # Start Webcam 
# cap = cv.VideoCapture(0)
# count = 0
# max_images = 25

# while True:
#     ret, frame = cap.read()
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     # Detects face in gray image
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#     for(x,y,w,h) in faces:
#         # Draw rectangle around face
#         cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

#         # extract face region 
#         face_roi = gray[y:y+h, x:x+w]
#         face_roi = cv.resize(face_roi, (200,200))

#         # save image
#         file_name = os.path.join(person_path, f"{count}.jpg")
#         cv.imwrite(file_name,face_roi)
#         count += 1

#         cv.putText(frame, f"Saved: {count}", (10,30), cv.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)

#     cv.imshow("Collecting Faces", frame)

#     if cv.waitKey(1) & 0xff == ord('q') or count >= max_images:
#         break

# cap.release()
# cv.destroyAllWindows()


# ---------------------------- #
# Step 2 - Train the face using LBPH #
# ---------------------------- #

# # path to dataset directory 
# dataset_path = 'Saved_faces'

# # Create lists to store face images and labels
# faces = []
# labels = []

# # dictionary to map label number to person name 
# label_to_name = {}
# current_label = 0

# # Loop through each person folder
# for person_name in os.listdir(dataset_path):
#     person_path = os.path.join(dataset_path, person_name)
#     if not os.path.isdir(person_path):
#         continue # skip if not a folder

#     label_to_name[current_label] = person_name
#     for image_name in os.listdir(person_path):
#         image_path = os.path.join(person_path, image_name)

#         # Read the image in grayscale
#         image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
#         if image is None:
#             continue

#         faces.append(image)
#         labels.append(current_label)

#     current_label += 1

# # convert labels list to numpy array
# labels = np.array(labels)

# # create the LBPH face recognizer
# face_recognizer = cv.face.LBPHFaceRecognizer_create()

# # Train the recognizer with faces and labels
# face_recognizer.train(faces, labels)

# # Save the trained model 
# face_recognizer.write("Trained_model.yml")

# # Also save the label-name mappping 
# with open("labels.txt", "w") as f:
#     for label, name in label_to_name.items():
#         f.write(f"{label}:{name}\n")

# print("Training completed and model saved!")
