import cv2 as cv

img = cv.imread(r"opencv\images\building.jpg")

resize = cv.resize(img, (800,700))

gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)

blurred_img = cv.GaussianBlur(gray, (1, 1), 0)

# canny
edges = cv.Canny(blurred_img, 100,200)

contures_canny, _ = cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 
count = len(contures_canny)

# Thresold
thres_val, thres_img = cv.threshold(blurred_img, 150, 220, cv.THRESH_BINARY)
conture_thres, _ = cv.findContours(thres_img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count2 = len(conture_thres)

print(count2)
print(count)


# Draw the Contures
img_thres = resize.copy()
img_canny = resize.copy()

cv.drawContours(img_canny, contures_canny, -1, (0, 255, 0), 2)

cv.drawContours(img_thres, conture_thres, -1, (0, 0, 255), 2)

cv.imshow("Conture Thresh",img_thres)
cv.imshow("Conture Canny",img_canny)

cv.waitKey(0)
cv.destroyAllWindows()