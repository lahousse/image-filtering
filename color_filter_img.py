################ Henri Lahousse ################
# color filtering on image
# 05/31/2022

# libraries
import cv2 as cv
import numpy as np

#read the image
img = cv.imread(r"C:\Users\Goedele\Documents\Downloads\bl.jpg")

#convert the BGR image to HSV colour space
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#set the lower and upper bounds for the green hue
lower_green = np.array([204, 204, 0]) # 153, 153, 0
upper_green = np.array([255, 255, 204])

#create a mask for green colour using inRange function
mask = cv.inRange(img, lower_green, upper_green)

#perform bitwise and on the original image arrays using the mask
res = cv.bitwise_and(img, img, mask=mask)

#create resizable windows for displaying the images
cv.namedWindow("res", cv.WINDOW_NORMAL)
cv.namedWindow("hsv", cv.WINDOW_NORMAL)
cv.namedWindow("mask", cv.WINDOW_NORMAL)

#display the images
cv.imshow("mask", mask)
cv.imshow("hsv", hsv)
cv.imshow("res", res)

cv.imwrite(r"ENTER_PATH", res) # save result

if cv.waitKey(0):
    cv.destroyAllWindows()

