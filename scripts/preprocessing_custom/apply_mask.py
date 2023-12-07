import argparse
import cv2
import numpy as np

def apply_mask(img, mask, alpha=False):
    # Apply mask on input image
    masked_img = cv2.bitwise_and(img, img, mask=mask)

    # Set masked out part of the image to transparent if alpha flag is set
    if alpha:
        alpha_mask = cv2.bitwise_not(mask)
        alpha_channel = np.ones(masked_img.shape[:2], dtype=masked_img.dtype) * 255
        alpha_channel[alpha_mask == 255] = 0
        masked_img[:,:,3] = alpha_channel

    return masked_img

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Apply mask on input image and save it in output file')
    
    # Add arguments
    parser.add_argument('-in', '--input', type=str, required=True, help='Path to input file')
    parser.add_argument('-out', '--output', type=str, required=True, help='Path to output file')
    parser.add_argument('-mask', '--mask', type=str, required=True, help='Path to mask file')
    parser.add_argument('-a', '--alpha', action='store_true', help='Set masked out part of the image to transparent')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Read input image and mask
    img = cv2.imread(args.input)
    mask = cv2.imread(args.mask, 0)
    
    # Apply mask to input image and save masked image to output file
    masked_img = apply_mask(img, mask, args.alpha)
    
    # Save masked image to output file
    cv2.imwrite(args.output, masked_img)
