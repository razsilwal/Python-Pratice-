import cv2 as cv

img = cv.imread(r"opencv\images\building.jpg")

## it show the real image
# cv.imshow("Original", img)


## Resize the image
resized = cv.resize(img, (400, 300)) # width and height
# cv.imshow("Resized", resized)


## Covert to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)


## crop the image [y1:y2, x1:x2]
cropped = img[600:900, 600:900] # adjust values as needed 
# cv.imshow("Cropped", cropped)

## Draw on the image (copy first to avoid changing original)
img_copy = img.copy()

## Draw a rectangle: (image, start_point, endpoint, color, thickness)
cv.rectangle(img_copy, (200,100), (500,300), (0,255,0))


## Draw a circle: (image, center, radius, color, thickness)
cv.circle(img_copy, (400,250),40, (255,0,0), 2)

## Draw a line: (image, startpoint, endpoint, color, thickness)
cv.line(img_copy, (200,100),(500,300), (0,0,255), 2)

## Put text: (image, text, position, font, size, color, thickness)
cv.putText(img_copy, "Building", (280,90), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),2)

# cv.imshow("copy Image", img_copy)


## Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

## Apply different Blurs 
## 3a. Gaussian Blur(src, ksize, sigmaX)
## ksize = kernel size(must be odd), sigmaX = Gaussian kernel std deviation in X 

gauss = cv.GaussianBlur(gray, (9,9),3)
# cv.imshow("Gaussian Blur", gauss) 

## 3b. Median Blur (src.ksize)
## ksize must be an odd interger > 1; good for removing salt-and-pepper noise
median = cv.medianBlur(gray, 5)
# cv.imshow("Median Blur", median)


## 3c. Bilateral Filter (src, d, sigmacolor, sigmaspace)
## d- diameter of pixel, sigmacolor- how much color difference, sigmaspace - how far pixels influence
bilateral = cv.bilateralFilter(gray, 11, 100, 100)
# cv.imshow("Bilateral Blurr", bilateral)

# --------------------------------#
# step 4: Apply edge detection
# -------------------------------- #

## 4a. Sobel Edge Detection(1st derivative)
## cv.Sobel(src, ddepth, dx, dy, ksize)
# ddepth- output image depth, dx - order of derivative X, dy- order of derivative Y

sobelx = cv.Sobel(gauss, cv.CV_64F, 1, 0) # vertical edges 
sobely = cv.Sobel(gauss, cv.CV_64F, 0, 1) # horizontal edge

## convert results to 8 bit and combine them 
sobelx_abs = cv.convertScaleAbs(sobelx)
sobely_abs = cv.convertScaleAbs(sobely)
combined = cv.bitwise_or(sobelx_abs, sobely_abs)
# cv.imshow("Sobel Edge", combined)


## 4b. Laplacian Edge Detection (2nd derivative)
## cv.Laplacian(src, depth)
laplacian = cv.Laplacian(gauss, cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian)
# cv.imshow("Laplacian Edge", laplacian)


## 4c. Canny Edge Detection( best quality)
## cv.Canny(image, threshold1, threshold2)
# threshold1 = lower bound, threshold2 = upper bound
# edges stronger than threshold2 kept, and connected weak edges are connecte too  
canny = cv.Canny(gauss, 100,200)
cv.imshow("Canny Edge", canny)

# ------------------------------- #
## step 5 : Find counters
# ------------------------------- #

counters, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)



cv.waitKey(0)
cv.destroyAllWindows()