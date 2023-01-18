import cv2
import numpy as np
from skimage.util import random_noise
import pathlib

files = list(pathlib.Path("./Inputs").rglob("*.png"))
save_original_to = "./Original/"
save_noisy_to = "./Noisy/"

for i in files:

    p = pathlib.Path(save_noisy_to + i.stem)
    p.mkdir(parents=True, exist_ok=True)

    extension = i.suffix

    img = cv2.imread(str(i))

    original = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    cv2.imwrite(save_original_to + i.name, original)

    snp06 = random_noise(original, mode="s&p", amount=0.06)
    snp06 = np.array(255*snp06, dtype='uint8')

    cv2.imwrite( str(p) + "/salt_and_pepper_0.06" + extension, snp06)

    
    snp005 = random_noise(original, mode="s&p", amount=0.005)
    snp005 = np.array(255*snp005, dtype='uint8')

    cv2.imwrite(str(p) + "/salt_and_pepper_0.005" + extension, snp005)

    gaussian001 = random_noise(original, mode="gaussian", mean=0, var=0.001)
    gaussian001 = np.array(255*gaussian001, dtype='uint8')

    cv2.imwrite(str(p) + "/gaussian_0.001" + extension, gaussian001)


    gaussian03 = random_noise(original, mode="gaussian", mean=0, var=0.03)
    gaussian03 = np.array(255*gaussian03, dtype='uint8')

    cv2.imwrite(str(p) + "/gaussian_0.03" + extension, gaussian03)
    


