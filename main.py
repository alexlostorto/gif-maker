import os

from src.files import traverse
from src.camera import takePicture
from src.gif import *


ROOT = r"C:\Users\[Users]\[pythonFiles]"


def main():
    assert os.path.isdir(ROOT)

    saveDir = traverse(ROOT, "Choose save directory (press ENTER to choose CWD): ")
    takePicture(saveDir)


if __name__ == '__main__':
    main()
