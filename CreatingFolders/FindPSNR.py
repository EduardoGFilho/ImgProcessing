import cv2
import numpy as np
import pathlib



files = list(pathlib.Path("./Original").rglob("*.png"))

txt = open("PSNR.txt","w")

for i in files:
    original = cv2.imread(str(i))

    txt.write(i.name)
    txt.write("\n")

    noisy = list(pathlib.Path("./Noisy/" + i.stem).rglob("*.png"))

    for j in noisy:

        im_noisy = cv2.imread(str(j))
        v_PSNR = cv2.PSNR(original, im_noisy)
        print(j.name)
        print(v_PSNR)
        txt.write("\t")
        txt.write(j.name)
        txt.write(": ")        
        txt.write(str(v_PSNR))
        txt.write("\n")



    filtered = list(pathlib.Path("./Filtered/" + i.stem).rglob("*.png"))
    for j in filtered:
        im_filtered = cv2.imread(str(j))
        v_PSNR = cv2.PSNR(original, im_filtered)
        print(j.name)
        print(v_PSNR)
        txt.write("\t")
        txt.write(j.name)
        txt.write(": ")        
        txt.write(str(v_PSNR))
        txt.write("\n")
    