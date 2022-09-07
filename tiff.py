from PIL import Image
# import os
# os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,70).__str__()
import cv2
# try:
img = cv2.imread("testTiff_1.tiff", cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey(0)
# # im = Image.open('first.tif')
# # im.show() except:
#     print("exception")
# print(img.shape)
# # bigger = cv2.resize(img, (300, 300))

#

# import numpy as np
# from skimage.io import imread

# img = imread('testTiff_1.tiff')
# print(img)