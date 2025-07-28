import cv2 as cv
import numpy as np 

img = cv.imread(r"opencv\images\building.jpg")
cv.imshow("Image", img)

# It converts the pict into gray color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian Method
# lap = cv.Laplacian(gray, cv.CV_64F) # second derivative -> +ve and -ve 
# lap = np.uint8(np.absolute(lap)) # unsigned integer8 memory should be low  
# cv.imshow("Laplacian", lap)

# Sobel Method

sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)

# cv.imshow("Sobel X", sobel_x) # 
# cv.imshow("Sobel Y", sobel_y)

# combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
# combined_sobel = np.uint8(np.absolute(combined_sobel))
# cv.imshow("Combined Sobel", combined_sobel)

# Canny 
edges = cv.Canny(gray, threshold1=50, threshold2=300)
cv.imshow("Canny", edges)
cv.waitKey(0)
