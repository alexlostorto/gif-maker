import os
import cv2
import numpy as np


def takePicture(saveDir, fileName):
    # For devices with multiple cameras
    cameraPort = 0
    camera = cv2.VideoCapture(cameraPort)

    result, image = camera.read()

    if result:
        cv2.imshow("opencvtest", image)
        cv2.imwrite(os.path.join(saveDir, fileName), image)

        # Press Esc key to exit
        if cv2.waitKey(1) == 27:
            cv2.destroyWindow("opencvtest")
    else:
        print("No image detected. Please! try again")
