import cv2 as cv

img = cv.imread(r"opencv\images\WIN_20230422_12_18_13_Pro.jpg")
resized = cv.resize(img, (900,900))
cv.imshow("Image", resized)

# # Average Blurring
# avg_blur = cv.blur(resized, (9,9))
# cv.imshow("Average Blur", avg_blur)


# Median Blur

# median_blur = cv.medianBlur(resized, 11)
# cv.imshow("Median Blur", median_blur)

# Gaussain Blur
# Gauss_blur = cv.GaussianBlur(resized, (9,9), 9)
# cv.imshow("Gaussian Blur", Gauss_blur)


# Bilateral Blur 
bilateral = cv.bilateralFilter(resized, 5, 15, 15)
cv.imshow("Billateral Show", bilateral)


cv.waitKey(0)