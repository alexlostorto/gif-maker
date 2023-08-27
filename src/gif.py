import os
import imageio
from datetime import datetime


def createGIF(saveDir, files):
    images = [imageio.imread(f) for f in files]

    now = datetime.now()
    fileName = now.strftime(f"%d-%m-%Y %H-%M-%S.gif")

    imageio.mimsave(os.path.join(saveDir, fileName), images, duration=0.5)

    print(f"GIF Saved as {fileName}")


def deleteFiles(files):
    for file in files:
        os.remove(file)
