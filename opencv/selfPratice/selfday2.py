import cv2 as cv

# open webcam 
# cap = cv.VideoCapture(0) # 0 default webcam

# while True:
#     ret, frame = cap.read() # Read frame from webcam
#     cv.imshow("Live Feed", frame)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release() # it close camera
# cv.destroyAllWindows() # it close window


# ------------------------ #
# --face, smile and eye -- #
# ------------------------ # 
# # load the face detection model (Haar cascade)
# face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # load for eye cascade
# eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')


# # load for smile cascade
# smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')

# # start a webcam
# cap = cv.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     # convert to grayscale
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     # detect Faces: return list of rectangles [x,y,w,h]
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#     # draw rectangle on each face
#     for(x, y, w, h) in faces:
#         cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

#         # region of interest (ROI) for face
#         roi_gray = gray[y:y + h, x:x + w]
#         roi_color = frame[y:y + h, x:x + w]

#         # detect eyes inside face region
#         eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=8)
#         for(ex,ey,ew,eh) in eyes:
#             cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,0,255),2)

#         # detect smile inside the face
#         smiles = smile_cascade.detectMultiScale(
#             roi_gray, scaleFactor=1.7, minNeighbors=20
#         )
#         for(sx,sy,sw,sh) in smiles:
#             cv.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255,0,0),2)
#     cv.imshow("Face, Smile and Eye Detection",frame)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()


# ---------------------- #
# --- Face blurring ---- #
# ---------------------- #
# face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#     for(x,y,w,h) in faces:
#         # extract the face region
#         face_region = frame[y:y+h, x:x+w]

#         # apply a strong blur to the face
#         blurred_face = cv.GaussianBlur(face_region, (99,99),30)

#         # replace  the original face region with blurreed version
#         frame[y:y+h, x:x+w] = blurred_face

#     cv.imshow("Face Blurring", frame)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv.destroyAllWindows()


# ------------------------------ #
# --saving detected face images -#
#--------------------------------#

# import cv2 as cv
# import os 

# face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # create directory to save images
# save_dir = "Saved_faces"
# os.makedirs(save_dir, exist_ok=True)

# cap = cv.VideoCapture(0)
# count = 0
# max_faces = 30 # max number of images to save

# while True:
#     ret, frame = cap.read()

#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

#     for (x,y,w,h) in faces:
#         # extract face region
#         face_img = frame[y:y+h, x:x+w]

#         #resize faces to a fixed size
#         face_img = cv.resize(face_img, (200,200))

#         # save the face image
#         file_path = os.path.join(save_dir, f"face_{count}.jpg")
#         cv.imwrite(file_path, face_img)
#         count += 1

#         # draw a rectangle and show count
#         cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
#         cv.putText(frame, f"Saved: {count}", (10,30), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

#     cv.imshow("Saving Faces", frame)

#     if cv.waitKey(1) & 0xFF == ord('q') or count >= max_faces:
#         break

# cap.release()
# cv.destroyAllWindows()
