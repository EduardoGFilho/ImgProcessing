# %%
import numpy as np
import scipy.signal as signal
import scipy.ndimage as ndimage
import cv2
from statistics import median


# %%
a = [1, 3, 5, 6, 5, 7]
a.sort()


# %%
def unsharpMask():
    u = signal.unit_impulse(shape=(3, 3), idx="mid", dtype=np.int8)
    l = ndimage.laplace(u)
    return u - l


def averageMask(M):
    return (np.ones((M, M)))*(1/M)


# %%
def median_filter(img, filter_size):
    img = np.array(img)
    img_final = img
    indexer = filter_size // 2

    for img_column in range(img.shape[0]):
        for img_row in range(img.shape[1]):
            tmp = []

            for filter_column in range(filter_size):
                for filter_row in range(filter_size):

                    i = img_column + filter_column - indexer
                    j = img_row + filter_row - indexer
                    
                    if i >=0 and j >= 0 and i < img.shape[0] and j < img.shape[1] :
                        tmp.append(img[i][j])
            tmp.sort()
            img_final[img_column][img_row] = tmp[len(tmp) // 2]
    return img_final


# %%
img = cv2.imread("moon.png")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_filtered = median_filter(img, 5)
cv2.imwrite("abacate.png", img_filtered)



