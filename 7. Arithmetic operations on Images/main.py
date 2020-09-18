import cv2
import numpy as np


image_1 = cv2.imread("original_image_1.jpg")
image_2 = cv2.imread("original_image_2.jpg")
# Both images should have same dimension


# Weighted sum
weighted_image = cv2.addWeighted(image_1, 0.5, image_2, 0.5, 0)
# new image will be like (image_1 * 0.5) + (image_2 * 0.5) + 0
# result values will be scalled to max value of original image


# Sum
added_image = cv2.add(image_1, image_2)
# new image will be like (image_1 + image_2)
# result values will be scalled to max value of original image


# Subtraction
subtracted_image = cv2.subtract(image_1, image_2)
# new image will be like (image_1 - image_2)
# result values will be scalled to max value of original image


# Displaying images
cv2.imshow("Weighted image", weighted_image)
cv2.imshow("Added image", added_image)
cv2.imshow("Subtracted image", subtracted_image)


cv2.waitKey(0)