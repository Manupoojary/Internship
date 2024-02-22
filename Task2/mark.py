import cv2
import numpy as np

def point(rotated_image,thinnest_point):
    # Resize the ruler image to match the width of the rotated image
    ruler_image=cv2.imread('focal.jpg')
    resized_ruler_image = cv2.resize(ruler_image, (rotated_image.shape[1], ruler_image.shape[0]))
    # Calculate the position of the thinnest point in the original image coordinates
    thinnest_point_original = (int(thinnest_point[0] * (resized_ruler_image.shape[1] / rotated_image.shape[1])), int(thinnest_point[1] * (resized_ruler_image.shape[0] / rotated_image.shape[0])))

    # Draw a vertical line on the ruler image at the position of the thinnest point
    cv2.line(resized_ruler_image, (thinnest_point_original[0], 0), (thinnest_point_original[0], resized_ruler_image.shape[0]), (0, 0, 255), 2)

    # Vertically concatenate the rotated image and the resized ruler image
    concatenated_image = np.vstack((resized_ruler_image,rotated_image))

    cv2.imshow("final Image",concatenated_image)
    cv2.waitKey(0)


if __name__=="__main__":
    def __init__(self,rotated_image,thinnest_point):
        point(rotated_image,thinnest_point)
