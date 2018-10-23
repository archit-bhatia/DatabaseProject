import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("FaceID.png",flags=0)

'''Display Image
plt.figure(0)
print (img)
plt.imshow(img, cmap='gray')
plt.show()
'''
def face_verify():
    img = cv2.imread("FaceID.png",0)
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img = img.reshape((img.shape[0]*img.shape[1],))
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("test", gray)
        if not ret:
            break

        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:

            # SPACE pressed
            gray = gray.reshape((gray.shape[0]*gray.shape[1],))
            print(np.mean(img-gray))

    cam.release()
    cv2.destroyAllWindows()


img = cv2.imread("FaceID.png",0)
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("test", gray)
        if not ret:
            break

        k = cv2.waitKey(1)

        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:

            # SPACE pressed
            cv2.imwrite("FaceID.png",gray)

    cam.release()
    cv2.destroyAllWindows()
