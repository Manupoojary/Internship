import cv2
import thin_point_finder as tf
cam =cv2.VideoCapture(0)
import os

count=0

while True:
    ret,img = cam.read()
    cv2.imshow("Test",img)

    if not ret:
        break
    k=cv2.waitKey(1)
    #For Esc key
    if k%256==27:
        print("Close")
        break

    elif k%256==32:
        #For Space key
        print("Image "+str(count)+"saved")
        file='images/img'+str(count)+'.jpg'
        cv2.imwrite(file,img)
        count+=1
        # tf.main(file)
cam.release()
cv2.destroyAllWindows() 
tf.main()
