import cv2
import numpy as np
from apply_mask import apply_mask
import os

import argparse

parser = argparse.ArgumentParser(description='Process input arguments.')
parser.add_argument('--input', type=str, help='the path to the input file', required=True)
parser.add_argument('--output', type=str, help='the path to the output folder', required=True)
parser.add_argument('--crop', type=bool, help='Crop the image around the statue 0 or 1', default=False)
parser.add_argument('--margin', type=int, help='The cropping padding', default=0)
parser.add_argument('--contour', type=int, help='The contour to use, area in descending order', default=0)

# Uncomment the appropriate line to parse arguments when running from the command line or debugging
# Parse arguments when running from the command line
args = parser.parse_args()
# Default arguments for debugging:
#args = argparse.Namespace(input='/data/sandor/images/monopointcloud/preprocessing/70.png', output='/data/sandor/images/monopointcloud/preprocessing', crop=False, margin=0)

# Input images required in the folder:
# - <image_name>_masked.png
# - <image_name>_semseg.png
# - <image_name>.png

# Input image path
input_file = os.path.abspath(args.input)
# Output folder path
output_folder = os.path.abspath(args.output)
# Flag defining if the images should be cropped to the contour bounding box
crop = args.crop
# Padding around the bounding box
padding = args.margin
# Contour to use, area in descending order
contour_idx = args.contour

# Extract the path where the image is located
input_path = os.path.dirname(input_file)
# Extract the image number from the input path
img_name =os.path.basename(os.path.splitext(input_file)[0])

# Load the masked image
# /data/sandor/images/monopointcloud/preprocessing/70_masked.png
masked_img_path = os.path.join(input_path, f'{img_name}_masked.png')
masked_img = cv2.imread(masked_img_path, cv2.IMREAD_UNCHANGED)
# Create a mask where the transparent part of the image is the sky
sky_mask = np.zeros(masked_img.shape[:2], dtype=np.uint8)
sky_mask[masked_img[:,:,3] != 0] = 255

# Load the segmented image
segmented_path = os.path.join(input_path, f'{img_name}_semseg.png')
segmented_img = cv2.imread(segmented_path, cv2.IMREAD_UNCHANGED)

# Create a mask for objects which are black (0, 0, 0)
black_mask = cv2.inRange(segmented_img, (0, 0, 0), (0, 0, 0))
# Make a bitwise and with the sky mask
black_mask = cv2.bitwise_and(black_mask, black_mask, mask=sky_mask)

# Find the contours in the black mask
contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Sort contours based on their area
contours = sorted(contours, key=cv2.contourArea, reverse=True)
# Create a mask for the largest contour
largest_contour_mask = np.zeros(black_mask.shape, dtype=np.uint8)
cv2.drawContours(largest_contour_mask, contours, contour_idx, 255, -1)

# Make a bitwise and with the black mask
largest_contour_mask = cv2.bitwise_and(largest_contour_mask, largest_contour_mask, mask=black_mask)

# Load rgb image
rgba_img = cv2.imread(input_file, cv2.IMREAD_UNCHANGED)

# Apply the largest contour mask on the rgb image
rgba_masked = apply_mask(rgba_img, largest_contour_mask, alpha=True)

# Crop the images if the crop flag is set
if crop:
    # Find the bounding box of the largest contour
    x, y, w, h = cv2.boundingRect(contours[contour_idx])
    # Add padding to the bounding box
    x -= padding
    y -= padding
    w += 2*padding
    h += 2*padding
    # Crop the masked rgb image
    rgba_masked = rgba_masked[y:y+h, x:x+w]
    # Crop the original rgb image
    rgba_img = rgba_img[y:y+h, x:x+w]
    out_crop_path = os.path.join(output_folder, f"{img_name}_rgba_cropped.png")
    cv2.imwrite(out_crop_path, rgba_img)

# Save the masked rgba image
out_rgb_path = os.path.join(output_folder, 'rgba.png')
cv2.imwrite(out_rgb_path, rgba_masked)
