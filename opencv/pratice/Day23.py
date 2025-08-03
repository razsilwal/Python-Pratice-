# Bitwise operation and masking

import cv2 as cv
import numpy as np 

# # Create two blank images
# img1 = np.zeros((300,300), dtype="uint8")
# img2 = np.zeros((300,300), dtype="uint8")

# # Draw a rectangle on image 1
# cv.rectangle(img1, (50,50), (250,250),255,-1)

# # Draw a circle on image 2
# cv.circle(img2, (150,150), 120, 255, -1)

# cv.imshow("Rectange Image 1",img1)
# cv.imshow("Circle Image 2",img2)

# # AND operation It print the intersection of img1 and img2
# bit_and = cv.bitwise_and(img1, img2)
# cv.imshow("AND", bit_and)

# # OR operation it print the combination of img1 and img2
# bit_or = cv.bitwise_or(img1, img2)
# cv.imshow("OR", bit_or)

# # XOR operation
# bit_xor = cv.bitwise_xor(img1, img2)
# cv.imshow("XOR", bit_xor)

# # NOT operation It reverse the image color 
# bit_not = cv.bitwise_not(img2)
# cv.imshow("NOT", bit_not)

# cv.waitKey(0)
# cv.destroyAllWindows()


## Masking 

# img = cv.imread(r"opencv\images\20240305_170014.jpg")
# # cv.imshow("Original", img)

# # Resize the image
# resize = cv.resize(img, (800,600))
# cv.imshow("Image", resize)

# # Create a Mask
# img_mask = np.zeros(resize.shape[:2], dtype="uint8")

# # Create a white circle in the mask 
# cv.circle(img_mask, (350,200), 100, 255, -1)

# # Apply the Mask 
# masked_img = cv.bitwise_and(resize, resize, mask=img_mask)

# # cv.imshow("Mask Image", img_mask)
# cv.imshow("Masked Image", masked_img)

## ------------------------- ##
## ------ Color Channels --- ##
## ------------------------- ##

img = cv.imread(r"opencv\images\building.jpg")
# cv.imshow("Original", img)

# Resize the image
resize = cv.resize(img, (800,600))
cv.imshow("Image", resize)

# Splitting the channels
B, G, R = cv.split(resize)

# cv.imshow("Gray -> Blue", B)
# cv.imshow("Gray -> Green", G)
# cv.imshow("Gray -> Red", R)

# # merged all color
# merged = cv.merge([B, G, R])
# cv.imshow("Merged Image",merged)

# zeros = np.zeros_like(B)
# blue_visual = cv.merge([B, zeros, zeros])
# green_visual = cv.merge([zeros, G, zeros])
# red_visual = cv.merge([zeros, zeros, R])

# cv.imshow("Blue Visual",blue_visual)
# cv.imshow("Green Visual",green_visual)
# cv.imshow("Red Visual",red_visual)

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
blue_visual = cv.merge([B, gray, gray])
cv.imshow("Blue Visuals", blue_visual)



cv.waitKey(0)
cv.destroyAllWindows()
