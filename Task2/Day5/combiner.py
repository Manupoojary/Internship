import cv2    
import numpy as np
import math
import point_finder

def main(rotated_image, thinnest_point):
    ruler_image = cv2.imread('focal.jpg')
    if ruler_image is None:
        print("Error: Unable to load ruler image.")
        return

    # Resize the ruler image to match the width of the rotated image
    resized_ruler_image = cv2.resize(ruler_image, (rotated_image.shape[1], ruler_image.shape[0]))
    # Calculate the position of the thinnest point in the original image coordinates
    orgi_img_thinnest_point = (int(thinnest_point[0] * (resized_ruler_image.shape[1] / rotated_image.shape[1])), int(thinnest_point[1] * (resized_ruler_image.shape[0] / rotated_image.shape[0])))

    # Draw a vertical line on the ruler image at the position of the thinnest point
    cv2.line(resized_ruler_image, (orgi_img_thinnest_point[0], 0), (orgi_img_thinnest_point[0], resized_ruler_image.shape[0]), (0, 0, 255), 2)

    # Vertically concatenate the rotated image and the resized ruler image
    combined_image = np.vstack((resized_ruler_image,rotated_image))
    # total_parts = 9
    # part_width = resized_ruler_image.shape[1] / total_parts
    # value = math.ceil(orgi_img_thinnest_point[0] / part_width)
    # print(f"Thin line is at the point: {value}mm")

    point_finder.point(resized_ruler_image,orgi_img_thinnest_point)
    return combined_image



if __name__ == "__main__":
    def __init__(self,rotated_image,thinnest_point):
     main(rotated_image, thinnest_point)
