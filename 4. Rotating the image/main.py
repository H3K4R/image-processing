import cv2


image = cv2.imread("original_image.jpg")


# Rotating an image
h, w = image.shape[:2]
center = (w // 2, h // 2)  # from where we want to rotate
angle = 45  # angle from which we want to rotate
scale = 1  # scale with which we want to

matrix = cv2.getRotationMatrix2D(center, angle, scale)
# you can have your own matrix as well

rotated_image = cv2.warpAffine(image, matrix, (w, h))
"""
alpha = scale*cos(angle)
beta = scale*cos(angle)

x, y = current pixel of image

matrix = [[alpha, beta,  (1 - alpha) * center * x - beta * center * y],
          [-beta, alpha, beta * center * x + (1 - alpha) * center * y]]

wrapaffine does fillowing for all pixel values
output = _x, _y = matrix cross [x,
                                y,
                                1]

here output is generated for all pixel values
and after combining them we get the new rotated image
"""


# Displaying rotated image
cv2.imshow("Rotated image", rotated_image)


cv2.waitKey(0)
