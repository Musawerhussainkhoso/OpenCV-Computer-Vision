import cv2
image = cv2.imread("brown-horse-with-white-star-isolated_1301368-57159.avif")
if image is None:
    print("Image not loaded!")
else:
    print("Image loaded successfully!")
    print(image.shape)