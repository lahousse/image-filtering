################ Henri Lahousse ################
# filter image contrast
# 05/31/2022

# libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# img is input photo
img = cv2.imread(r"ENTER_PATH")
lane_image = np.copy(img)

# grayscale
gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
plt.title('grayscale'), plt.xticks([]), plt.yticks([])
plt.show()

# GaussianBlur lessens storingen
blur = cv2.GaussianBlur(lane_image, (5, 5), 0)
plt.imshow(blur, cmap='gray')
plt.title('GaussianBlur'), plt.xticks([]), plt.yticks([])
plt.show()

# shows the curves
edges = cv2.Canny(blur,100,200)
plt.imshow(edges,cmap='gray')
plt.title('hoeken'), plt.xticks([]), plt.yticks([])
plt.show()

size = (277,182)
background = edges.resize(size,Image.ANTIALIAS)
img = img.resize(size,Image.ANTIALIAS)

#background.paste(img, (0, 0)) # paste image on top
background.save(r"ENTER_PATH") # save image