import cv2


image = cv2.imread("original_image.jpg")


# Extracting region of interest
roi = image[100:300, 200:400]


# Displaying extracted roi
cv2.imshow("Region of Interest", roi)


cv2.waitKey(0)
