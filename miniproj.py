import cv2
image = cv2.imread(r"D:\OpenCV\images.jfif" )
if image is None:
    print("Image not loaded!")
else:
    print("Image loaded successfully!")
    print(image.shape)
