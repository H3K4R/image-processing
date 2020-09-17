import cv2


image = cv2.imread("original_image.jpg")


# Writing on an image
output = image.copy()
text = "Hello!"
bottom_left_coordinates = (100, 200)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font_size = 5
font_color = (255, 0, 0)  # Blue
thickness = 6
cv2.putText(
    output,
    text,
    bottom_left_coordinates,
    font,
    font_size,
    font_color,
    thickness,
)  # inplace operation


# Displaying image
cv2.imshow("output", output)


cv2.waitKey(0)
