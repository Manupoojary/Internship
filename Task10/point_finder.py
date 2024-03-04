import math

def point(resized_ruler_image,orgi_img_thinnest_point):
    total_parts = 9
    part_width = resized_ruler_image.shape[1] / total_parts
    value = math.ceil(orgi_img_thinnest_point[0] / part_width)
    print(f"Thin line is at the point: {value}mm")
    return value

if __name__=="__main__":
    def __init__(self,resized_ruler_image,orgi_img_thinnest_point):
        point(resized_ruler_image,orgi_img_thinnest_point)