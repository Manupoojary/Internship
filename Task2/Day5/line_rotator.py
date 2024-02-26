import cv2
import numpy as np
import os
# Load the image

def rotate(image):
    image = image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection (if needed)
    canny_edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

    # Detect lines using Hough Line Transform
    detected_lines = cv2.HoughLines(canny_edges, 1, np.pi / 180, 100)

    # Draw detected lines on a copy of the original image
    line_image = np.copy(image)
    for line in detected_lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Straighten the detected line
    angle = theta * 180 / np.pi
    if angle <45:
        angle += 90
    else:
        angle -= 90

    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h), flags=cv2.INTER_LINEAR)
    return rotated_image

if __name__=="__main__":
    def __init__(self,imagepath):
        rotate(imagepath)
