import cv2
import numpy as np
import pathlib
from Filters import fspecialUnsharpen
from Filters import unsharpMask


files = list(pathlib.Path("./Inputs").rglob("*.png"))
files = list(pathlib.Path("./Inputs").rglob("*.jpeg"))

saveTo = "./Filtered/"

for i in files:

    extension = i.suffix

    img = cv2.imread(str(i))

    #kernel = fspecialUnsharpen(0.2)
    kernel = unsharpMask()

    img_sharp = cv2.filter2D(img, -1, kernel)
    cv2.imwrite(saveTo + i.name, img_sharp)
    


