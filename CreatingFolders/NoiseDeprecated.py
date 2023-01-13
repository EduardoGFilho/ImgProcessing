import cv2
import numpy as np
from skimage.util import random_noise
import pathlib

files = list(pathlib.Path("./Inputs").rglob("*.png"))
saveOriginalTo = "./Original/"
saveto = "./Noisy/"

for i in files:

    file = str(i)
    extension = str(i.suffix)
    name = str(i.stem)

    img = cv2.imread(file)

    original = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    cv2.imwrite(saveOriginalTo + name + "_original" + extension, original)

    snp06 = random_noise(original, mode="s&p", amount=0.06)
    snp06 = np.array(255*snp06, dtype='uint8')

    cv2.imwrite(saveto + name + "_snp06" + extension, snp06)

    snp005 = random_noise(original, mode="s&p", amount=0.005)
    snp005 = np.array(255*snp005, dtype='uint8')

    cv2.imwrite(saveto + name + "_snp005" + extension, snp005)

    gaussian001 = random_noise(original, mode="gaussian", mean=0, var=0.001)
    gaussian001 = np.array(255*gaussian001, dtype='uint8')

    cv2.imwrite(saveto + name + "_gaussian001" + extension, gaussian001)


    gaussian03 = random_noise(original, mode="gaussian", mean=0, var=0.03)
    gaussian03 = np.array(255*gaussian03, dtype='uint8')

    cv2.imwrite(saveto + name + "_gaussian03" + extension, gaussian03)


