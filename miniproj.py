import cv2
image = cv2.imread(r"D:\OpenCV\images.jfif" )
if image is not None:
   # print("Image not loaded!")
    cv2.imshow("Horse Picture" ,image)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    success = cv2.imwrite("output.jfif", image)

    if success:
        print("Image saved successfully!")
    else:
        print("Image could not be saved!")     
else:
    #print("Image loaded successfully!")
    print("image couldnt load")

