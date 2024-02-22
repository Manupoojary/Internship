import cv2
import numpy as np
import combiner
import line_rotator

image_path = 'line.jpg'

imgage = cv2.imread(image_path)
    
if imgage is None:
    raise ValueError(f"Error loading image: {image_path}")
gray = cv2.cvtColor(imgage, cv2.COLOR_BGR2GRAY)


# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)


# Detect lines using HoughLinesP
lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=100, maxLineGap=5)

if lines is None or len(lines) == 0:
    raise ValueError("No lines detected in the image.")

# Calculate the distance of each pixel on the line from the center of the image
image_center = (imgage.shape[1] // 2, imgage.shape[0] // 2)

def distance_from_center(x, y):
    return np.sqrt((x - image_center[0])*2 + (y - image_center[1])*2)

# Find the thinnest point on the line based on the distance from the center
thinnest_point = min(lines, key=lambda line: distance_from_center((line[0, 0] + line[0, 2]) // 2, (line[0, 1] + line[0, 3]) // 2))

# Draw a small circle at the thinnest point on the original image
img_thinnest = imgage.copy()
x, y = (thinnest_point[0, 0] + thinnest_point[0, 2]) // 2, (thinnest_point[0, 1] + thinnest_point[0, 3]) // 2
cv2.circle(img_thinnest, (x, y), 5, (0, 0, 255), -1)

cv2.imshow('Thin Point',img_thinnest)
cv2.waitKey(0)

rotated_image=line_rotator.rotate(img_thinnest)
combine_image=combiner.main(rotated_image,thinnest_point)
cv2.imshow('Combined Image',combine_image)
cv2.waitKey(0)

