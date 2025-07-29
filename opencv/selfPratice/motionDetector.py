import cv2 as cv
import time
import winsound

# open the webcam
cap = cv.VideoCapture(0)

# Initialize first frame to None
first_frame = None
recording = False
out = None
motion_timer = 0
video_index = 0


while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # blur to reduce noise and improve detection
    gray = cv.GaussianBlur(gray, (21,21),0)

    # set the first frame for refrence
    if first_frame is None:
        first_frame = gray
        continue

    # Compute difference between first frame and current frame
    delta_frame = cv.absdiff(first_frame, gray)

    # Apply thresold to highlight motion areas
    thres_frame = cv.threshold(delta_frame, 25,255,cv.THRESH_BINARY)[1]

    # Dilate the thresold image to fill in holes
    thres_frame = cv.dilate(thres_frame, None, iterations=2)

    # Find contours (moving areas)
    contours, _ = cv.findContours(thres_frame.copy(),
                                  cv.RETR_EXTERNAL,
                                  cv.CHAIN_APPROX_SIMPLE)
    motion_detected = False
    for contour in contours:
        if cv.contourArea(contour) <1000:
            continue # ignore small movements
        
        motion_detected = True

        # get the bounding box for the contour
        (x,y,w,h) = cv.boundingRect(contour)

        # Draw rectangle around motion area
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

        # Save frame with timestamp
        # timestamp = time.strftime("%Y%m%d-%H%M%S")
        # cv.imwrite(f"Saved_faces/motion_images/motion_{timestamp}.jpg", frame)
        
    if motion_detected:
        if not recording:
            # start Recording
            print("Motion Detected - Start Recording")
            fourcc = cv.VideoWriter_fourcc(*"XVID")
            out = cv.VideoWriter(f"Saved_faces/motion_images/motion_{video_index}.avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            video_index += 1
            recording = True
            motion_timer = time.time()
        
        out.write(frame)

        # Stop Recording if no motion for 5 seconds
        if recording and time.time() - motion_timer > 5:
            print("Stopped recording no motion found")
            recording = False
            out.release()
            first_frame = None # Rest frame

        # it beep sound when motion is detected 
        winsound.Beep(1000, 1000) # beep at 1000hz for 500ms

    cv.imshow("Motion Detector", frame)

    if cv.waitKey(1) & 0xff ==ord('q'):
        break

# Release everything
if recording:
    out.release()

cap.release()
cv.destroyAllWindows()