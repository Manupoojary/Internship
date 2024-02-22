import cv2    
import numpy as np

def main(rotated_image, thinnest_point):
    ruler_image = cv2.imread(r'focal.jpg')
    if ruler_image is None:
        print("Error: Unable to load ruler image.")
        return

    # # Resize the ruler image to match the width of the rotated image
    resized_ruler_image = cv2.resize(ruler_image, (rotated_image.shape[1], ruler_image.shape[0]))

    combined_image = np.vstack((resized_ruler_image, rotated_image))

    cv2.imshow('comb', combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

if __name__ == "__main__":
    def __init__(self,rotated_image,thinnest_point):
     main(rotated_image, thinnest_point)
