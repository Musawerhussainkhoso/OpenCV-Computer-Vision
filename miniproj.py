import cv2
image = cv2.imread(r"D:\OpenCV\image.png")
if image is None:
    print("Image not loaded!")
else:
    print("Image loaded successfully!")
    print(image.shape)