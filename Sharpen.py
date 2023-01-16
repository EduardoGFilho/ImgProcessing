import cv2
import numpy as np

"""
def fspecialUnsharpen(alpha):
    h = np.array([[-alpha, alpha-1, -alpha],
                [alpha-1, alpha + 5, alpha-1],
                [-alpha, alpha-1, -alpha]])
    return (1/(alpha+1))*h

"""


img = cv2.imread("moon.png")

kernel = fspecialUnsharpen(0.2)
img_sharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", img_sharp)
cv2.waitKey()