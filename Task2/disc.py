import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import math


def resize_image(image, target_height, target_width=None):
    if target_width is None:
        ratio = target_height / image.shape[0]
        target_width = int(image.shape[1] * ratio)
    return cv2.resize(image, (target_width, target_height))
def start(image,thinnest_point):
    # Load the thinnest point image
    image_path_thin = 'line.jpg'
    img_thinnest=image

    # Load and resize the focal ruler image
    image_path_ruler = 'focal.jpg'
    img_ruler = cv2.imread(image_path_ruler)

    # Check if the image loading was successful
    if img_ruler is None:
        raise ValueError("Error loading focal ruler image.")

    # Resize images to a common height and width
    common_height = 400
    common_width = max(img_thinnest.shape[1], img_ruler.shape[1])
    img_thinnest_resized = resize_image(img_thinnest, common_height, common_width)
    img_ruler_resized = resize_image(img_ruler, common_height, common_width)

    # Combine images with ruler positioned above the thinnest line
    combined_image = np.vstack([img_ruler_resized, img_thinnest_resized])

    # Find ruler position and mark on the image
    ruler_width_mm = 50  # Example ruler width in mm
    position_on_ruler = math.ceil((thinnest_point[0, 0] + thinnest_point[0, 2]) / img_thinnest_resized.shape[1] * ruler_width_mm)

    # cv2.putText(combined_image, f"{position_on_ruler} mm", (20, common_height + 50),
    #         cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Display the final composite image
    plt.imshow(cv2.cvtColor(combined_image, cv2.COLOR_BGR2RGB))
    plt.title('Composite Image with Ruler')
    plt.show()
    return

if __name__=="__main__":
    def __init__(self,path,thinnest_point):
        start(path,thinnest_point)