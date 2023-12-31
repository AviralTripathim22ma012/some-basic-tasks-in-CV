# -*- coding: utf-8 -*-
"""m22ma012_Q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1azYpRl57xa80RD7Ho8pziYgRB7DRCmbt

**Q1**
"""

import imutils as it
import cv2 as cv
from skimage.metrics import structural_similarity

img_1= cv.imread('/content/Capture_1.png')
img_2= cv.imread('/content/Capture_2.png')

grey_img_1= cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
grey_img_2= cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

(score, diff)= structural_similarity(grey_img_1, grey_img_2, full= True)
diff= (diff*255).astype("uint8")
print("struct5ural similarity= ", format(score))

threshold= cv.threshold(diff, 0, 128, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
countours= cv.findContours(threshold.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
countours= it.grab_contours(countours)

differences= 0

for c in countours:
  (x, y, w, h)= cv.boundingRect(c)
  area= w*h
  if area>= 10:
    differences= differences + 1
    cv.rectangle(img_1, (x,y), (x+w, y+h), (0, 0, 255), 2)
    cv.rectangle(img_2, (x,y), (x+w, y+h), (0, 0, 255), 2)

print("differences= ", differences)

from google.colab.patches import cv2_imshow
cv2_imshow(img_1)
cv2_imshow(img_2)
cv2_imshow(diff)
cv.waitKey()

'''First I cropped the given image into 2 images, between which the differences are to be spotted, 
then I converted both the images into grayscale, and used structural_simillarity( ) function to find the structural similarity between both the images 

The difference between the two images is then calculated and displayed as an image. 
The difference image is thresholded using Otsu's thresholding method, and contours are found in the thresholded image. 
The contours are filtered based on their areas, and if their area is greater than or equal to 10000, 
a rectangle is drawn around the contour in both the original images and the number of differences is incremented.
'''
