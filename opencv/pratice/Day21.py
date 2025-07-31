# 
import cv2 as cv
import numpy as np 

img = cv.imread(r"opencv/images/building.jpg")

# resize:
resized = cv.resize(img, (1200,1200), interpolation = cv.INTER_CUBIC)
# cv.imshow("Original Image", resized)
# cv.waitKey(0)


# Flipping 
# flipped = cv.flip(img, -1)
# cv.imshow("Flipped Image", flipped)
# cv.waitKey(0)


# # Cropping 
# crop = img[100:500, 200:900]
# cv.imshow("Crop Image", crop)
# cv.waitKey(0)

# def translate(img, x, y):
#     trans_mat = np.float64([[1,0,x], [0,1,y]])
#     dimension = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, trans_mat, dimension)

# translated = translate(img, 50,50)
# cv.imshow("Translated Image",translated)
# cv.waitKey(0)


def rotate(img, angel, rotpoint = None):
    (height, width) = img.shape[:2] # 0 -> height & 1 -> width

    if rotpoint is None:
        rotpoint = (width // 2, height // 2)
    
    rotmat = cv.getRotationMatrix2D(rotpoint, angel, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotmat, dimension)

rotated = rotate(img, 90)
cv.imshow("Original Image", img)
cv.imshow("Rotate Image", rotated)
cv.waitKey(0)

