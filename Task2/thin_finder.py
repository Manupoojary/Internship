import cv2
import numpy as np

def find_thinnest_point(extracted_line):
    # Convert the extracted line to grayscale
    gray = cv2.cvtColor(extracted_line, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the minimum area (thinnest line)
    min_contour = min(contours, key=cv2.contourArea)

    # Find the thinnest point on the contour
    min_point = min_contour[:, 0, :].squeeze()
    thinnest_point_index = np.argmin(np.linalg.norm(min_point - min_point[0], axis=1))
    thinnest_point = tuple(min_point[thinnest_point_index])

    return thinnest_point

def main(exctrected_line1):
    # Path to the extracted line image
    extracted_line_path = 'extracted_line.jpg'


    # Read the extracted line image
    extracted_line = exctrected_line1
    if extracted_line is None:
        print("Error: Unable to load extracted line image.")
        return

    # Find thinnest point on the extracted line
    thinnest_point = find_thinnest_point(extracted_line)

    if thinnest_point is not None:
        print("Thinnest point coordinates:", thinnest_point)

        # Draw a circle at the thinnest point
        cv2.circle(extracted_line, thinnest_point, 5, (0, 0, 255), -1)

        # Display the extracted line with thinnest point
        cv2.imshow('Extracted Line with Thinnest Point', extracted_line)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    def __init__(self,extrcted_line):
        main(extrcted_line)
