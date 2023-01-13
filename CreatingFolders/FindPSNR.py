import cv2
import numpy as np
import pathlib



files = list(pathlib.Path("./Original").rglob("*.png"))

for i in files:
    original = cv2.imread(str(i))

    noisy = list(pathlib.Path("./Noisy/" + i.stem).rglob("*.png"))

    for j in noisy:
        im_noisy = cv2.imread(str(j))
        v_PSNR = cv2.PSNR(original, im_noisy)
        print(j.name)
        print(v_PSNR)

    filtered = list(pathlib.Path("./Filtered/" + i.stem).rglob("*.png"))
    for j in filtered:
        im_filtered = cv2.imread(str(j))
        v_PSNR = cv2.PSNR(original, im_filtered)
        print(j.name)
        print(v_PSNR)
    