import cv2
import numpy as np
from scipy.ndimage import median_filter
import pathlib
from FiltersLib import averageMask


files = list(pathlib.Path("./Original").rglob("*.png"))

save_to = "./Filtered/"

M = (3, 5, 7)

for k in files:
    save_filtered_to = pathlib.Path(save_to + k.stem)
    save_filtered_to.mkdir(parents=True, exist_ok=True)

    noisy_images = list(pathlib.Path("./Noisy").rglob("*.png"))

    for j in noisy_images:

        file = str(j)
        extension = str(j.suffix)
        name = str(j.stem)

        img = cv2.imread(file)

        for i in M:
            kernel = averageMask(i)
            img_average = cv2.filter2D(img, -1, kernel)

            img_median = median_filter(img, size=i)

            cv2.imwrite(str(save_filtered_to)+ "/" + name +"_average_M=" + str(i) + extension, img_average)
            cv2.imwrite(str(save_filtered_to)+ "/" + name + "_median_M=" + str(i) + extension, img_median)



