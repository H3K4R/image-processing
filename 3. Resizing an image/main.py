import cv2


image = cv2.imread("original_image.jpg")


# Resizing
size = (400, 400)  # (width, height)
resized_image = cv2.resize(image, size)


# Displaying resized image
cv2.imshow("Resized image", resized_image)


# Resizing with same aspect ratio
h, w = image.shape[:2]
ratio = h / w
new_width = 400
size = (new_width, int(new_width * ratio))
resized_war_image = cv2.resize(image, size)


# Displaying image
cv2.imshow("Resized with same aspect ration", resized_war_image)


cv2.waitKey(0)
