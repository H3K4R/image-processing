import cv2

image = cv2.imread("original_image.jpg")

h, w, d = image.shape
print(f"Height: {h}, Width: {w}, Depth (channels): {d}")


# Extracting BGR components
B = image[:, :, 0]
G = image[:, :, 1]
R = image[:, :, 2]


# Displaying BGR components
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)


cv2.waitKey(0)
