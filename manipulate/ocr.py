from PIL import Image
import pytesseract
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
  help="path to input image to be OCR'ed")
args = vars(ap.parse_args())

colour_image = cv2.imread(args["image"])
image = cv2.cvtColor(colour_image, cv2.COLOR_BGR2GRAY)

filename = "temp_receipt.png"
cv2.imwrite(filename, image)

text = pytesseract.image_to_string(Image.open(filename))
print('sdfsdf')
print(text)
cv2.imshow('Image', image)
os.remove(filename)

cv2.waitKey(0)
