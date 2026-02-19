import cv2 
image = cv2.imread("dino.jpg")

if(image is not None):
    flipped_horizontal = cv2.flip(image,1)
    flipped_vertical = cv2.flip(image,0)
    flipped_both = cv2.flip(image,-1)

    cv2.imshow("Original image",image)
    cv2.imshow("Horizonatal Flipped image",flipped_horizontal)
    cv2.imshow("Vertically flipped image",flipped_vertical)
    cv2.imshow("Both sided flipped image",flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not loaded image")