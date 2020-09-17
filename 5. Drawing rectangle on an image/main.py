import cv2


image = cv2.imread("original_image.jpg")


# Drawing rectangle
output = image.copy()
pt1 = (100, 100)
pt2 = (300, 300)
color = (255, 0, 0)  # Blue
thickness = 2
cv2.rectangle(
    output, pt1, pt2, color, thickness
)  # inplace operation


# Displaying image
cv2.imshow("output", output)


cv2.waitKey(0)
