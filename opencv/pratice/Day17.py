import cv2 as cv

# Reading images

img = cv.imread(r"opencv\images\20240305_165813.jpg")
cv.imshow("Image", img)

# resized = cv.resize(img, (500, 500))
# cv.imshow("Image", resized)

# flipped = cv.flip(resized, -1) # horizontal - 1, vertical- 0, both = -1
# cv.imshow("Image", flipped)

# gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# cv.imshow("Image", gray)


# cv.rectangle(resized, (200, 200), (400,400), (255,0,0), 2)
# cv.imshow("Image", resized)


# edge detection 
# canny -> ml model -> pre trained

# edges = cv.Canny(resized, threshold1=50, threshold2=200)
# cv.imshow("Edges", edges)



cv.waitKey(0)
