# Threshold 

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"opencv\images\building.jpg")
resize = cv.resize(img, (400,400))
# gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Simple Threshold
# threshold, thres_img = cv.threshold(gray, 135, 255, cv.THRESH_BINARY)
# threshold, thres_img_inv = cv.threshold(gray, 135, 255, cv.THRESH_BINARY_INV)

# cv.imshow("Simple Threshold Image", thres_img)
# cv.imshow("Simple Threshold Inverse Image", thres_img_inv)

# Adaptive Threshold
# adp_thre_img_gauss = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# adp_thre_img_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
# cv.imshow("Adaptive Gauss Threshold", adp_thre_img_gauss)
# cv.imshow("Adaptive Mean Threshold", adp_thre_img_mean)

## color format
# BGR -> Default
# RGB -> Standard color model
# Gray -> GrayScale
# HSV -> Hue, Saturation, Value
# HLS -> Hue, Lightness and Saturation
# LAB -> Human Perception based model 
# YCrCb -> Luma, Chroma -> Video Compression

## Color Spaces
gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY) # -> Gray
hsv = cv.cvtColor(resize, cv.COLOR_BGR2HSV) # -> HSV
hls = cv.cvtColor(resize, cv.COLOR_BGR2HLS)
ycrcb = cv.cvtColor(resize, cv.COLOR_BGR2YCR_CB)
rgb = cv.cvtColor(resize, cv.COLOR_BGR2RGB)
lab = cv.cvtColor(resize, cv.COLOR_BGR2LAB)

# cv.imshow("Gray Image", gray)
# cv.imshow("HSV Image", hsv)
# cv.imshow("HLS Image", hls)
# cv.imshow("YCRVB Image", ycrcb)
cv.imshow("RGB Image", rgb)
# cv.imshow("LAB Image", lab)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)

## usaage of color
# face Detection -> GrayScale, YCrCb, HSV
# color segmentation -> HSV
# Thresholding -> Gray
# Object Tracking -> HSV, LAB
# Image/Video compression -> YCrCb
# Image/Enhancement -> LAB