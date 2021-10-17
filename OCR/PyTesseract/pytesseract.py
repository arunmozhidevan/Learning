# pip install pytesseract
# pip install opencv-python

import cv2
import pytesseract


def greyscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def blur(image):
    return cv2.medianBlur(image, 5)


img = cv2.imread('Sample_quote.jpg')
img_grey = greyscale(img)
img_thresh = threshold(img_grey)
img_noise = blur(img_thresh)
print(pytesseract.image_to_string(img))
