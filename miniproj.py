import cv2
image = cv2.imread(r"D:\OpenCV\images.jfif" )
if image is None:
    print("Image not loaded!")
else:
    print("Image loaded successfully!")
    print(image.shape)
cv2.imshow("Horse Picture" , image)
cv2.waitKey(0)
cv2.destroyAllWindows()    
