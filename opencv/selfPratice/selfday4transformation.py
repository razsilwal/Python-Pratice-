import cv2 as cv
import numpy as np 

img = cv.imread(r"opencv\images\20240305_170014.jpg")
# cv.imshow("Original Image", img)

# resize
resize = cv.resize(img, (500,500))
cv.imshow("Resize", resize)


# Traslate the image by x and y 
def translate(img, x, y):

    # create a translation matrix
    translation_matrix = np.float32([[1,0,x],[0,1,y]]) 

    # get the image dimensions (width and height)
    (width,height) = img.shape[1], img.shape[0]

    # Apply the translation using warpAffine
    translated_img = cv.warpAffine(img, translation_matrix, (width, height))

    return translated_img

# translate the image by 100 pixels to the right  and 50 pixels
translated_image = translate(resize, 100, 50)

# show the translated image 
cv.imshow(" Translated image", translated_image)
cv.waitKey(0)
cv.destroyAllWindows()