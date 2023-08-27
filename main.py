import os

from src.files import traverse
from src.camera import takePictures
from src.gif import createGIF, deleteFiles


ROOT = r"C:\Users\[Users]\[pythonFiles]"
TIMER = 2   # Seconds
DELAY = 50  # Milliseconds
AMOUNT = 20  # Number of frames


def main():
    assert os.path.isdir(ROOT)

    saveDir = traverse(ROOT, "Choose save directory (press ENTER to choose CWD): ")
    files = takePictures(saveDir, TIMER, DELAY, AMOUNT)
    createGIF(saveDir, files)
    deleteFiles(files)


if __name__ == '__main__':
    main()
