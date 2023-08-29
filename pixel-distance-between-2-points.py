# -*- coding: utf-8 -*-
"""m22ma012_Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aKwbtaP87zRg4XEqMJSD0pLbU0V2onXS

**Q2: FINDING DISTANCES ON A MAP**

**Q2**
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
''' Load the image'''
image = cv2.imread("/content/india-map.jpg")

''' Convert the image to grayscale'''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

''' Detect the points in the image using blob detection'''
detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(gray)

''' Calculate the distances between the points'''
distances = []
for i in range(len(keypoints)):
    for j in range(i + 1, len(keypoints)):
        x1, y1 = keypoints[i].pt
        x2, y2 = keypoints[j].pt
        distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distances.append(((x1, y1), (x2, y2), distance))

''' Print the distances'''
for (x1, y1), (x2, y2), distance in distances:
    print("Distance between points ({:.0f}, {:.0f}) and ({:.0f}, {:.0f}): {:.2f}".format(x1, y1, x2, y2, distance))

''' Display the image with the points'''
image = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()