import cv2
import numpy as np
from scipy.ndimage import median_filter
from statistics import mean
import pathlib


def fspecialAverage(M):
    h = np.ones((M, M))
    return h/(M**2)


files = list(pathlib.Path("./Original").rglob("*.png"))

saveto = "./Filtered/"

for k in files:
    p = pathlib.Path(saveto + k.stem)
    p.mkdir(parents=True, exist_ok=True)

    q = list(pathlib.Path("./Noisy").rglob("*.png"))

    for i in q:

        file = str(i)
        extension = str(i.suffix)
        name = str(i.stem)

        img = cv2.imread(file)

        M = (3, 5, 7)

        for j in M:
            kernel = fspecialAverage(j)
            img_average = cv2.filter2D(img, -1, kernel)

            img_median = median_filter(img, size=j)

            cv2.imwrite(str(p)+ "/" + name +"_average_M=" + str(j) + extension, img_average)
            cv2.imwrite(str(p)+ "/" + name + "_median_M=" + str(j) + extension, img_median)







"""
    if i == 3:
        #teste, calcular a PNSR
        original = cv2.imread("Teste.png",cv2.IMREAD_GRAYSCALE)
        img_median = cv2.imread(path + "_median_M=" + str(i) + "." + extension, cv2.IMREAD_GRAYSCALE)
        error = np.array(original - img_median)
        MSE = np.mean(error**2)
        PSNR = 10*np.log10((255*255)/MSE)
        print(PSNR)
"""