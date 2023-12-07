import cv2
from PIL import Image
import sys

if len(sys.argv) < 2:
    print("Please provide the path to the image file as an argument.")
    sys.exit()

image_path = sys.argv[1]

# Read the image using OpenCV
img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Get the shape of the image
print(f"Image shape: {img.shape}")

# Open the image using Pillow
pil_img = Image.open(image_path)

# Get the mode of the image
mode = pil_img.mode
print("Image mode: {}".format(mode))
