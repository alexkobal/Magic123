import cv2
import argparse
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input image")
ap.add_argument("-o", "--output", required=False, help="path to output image")
args = vars(ap.parse_args())

# read the input image
image = cv2.imread(args["input"])

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# invert the pixel values
inverted = 255 - gray

# if no output path is provided, save the image in the same folder as the input image
if args["output"] is None:
    output_path = os.path.join(os.path.dirname(args["input"]), "inverted.png")
else:
    output_path = args["output"]

# convert the inverted image back to BGR format
inverted = cv2.cvtColor(inverted, cv2.COLOR_GRAY2BGR)

# save the inverted image
cv2.imwrite(output_path, inverted)
