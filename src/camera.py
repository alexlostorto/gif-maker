import os
import cv2
import time
from datetime import datetime


def takePicture(camera, saveDir, fileName):
    result, image = camera.read()

    if result:
        cv2.imshow("opencvtest", image)
        cv2.imwrite(os.path.join(saveDir, fileName), image)
    else:
        print("No image detected. Please! try again")


def takePictures(saveDir, timer, delay, amount):
    # For devices with multiple cameras
    cameraPort = 0
    camera = cv2.VideoCapture(cameraPort)

    delay = delay / 1000
    files = []

    print("Get ready!")

    time.sleep(timer)

    for i in range(amount):
        now = datetime.now()
        fileName = now.strftime(f"%d-%m-%Y %H-%M-%S-{i}.png")
        files.append(os.path.join(saveDir, fileName))
        takePicture(camera, saveDir, fileName)
        print(f"Picture {i+1} taken")
        time.sleep(delay)

    return files
