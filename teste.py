# %%
from PIL import Image
import numpy
import numpy as np
import scipy.signal as signal
import scipy.ndimage as ndimage
import cv2
from statistics import median

# %%


def unsharpMask():
    u = signal.unit_impulse(shape=(3, 3), idx="mid", dtype=np.int8)
    l = ndimage.laplace(u)
    return u - l


def averageMask(M):
    return (np.ones((M, M)))*(1/M)


# %%

def median_filter(data, filter_size):
    TESTE = 9

    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = numpy.zeros((len(data),len(data[0])))
    for i in range(len(data)):
        for j in range(len(data[0])):
            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            data_final[i][j] = median(temp)
            temp = []
    return data_final

# %%
img=cv2.imread("moon.png", -1)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_filtered=median_filter(img, 5)

# %%
cv2.imshow("Filtered Image", img_filtered)
cv2.waitKey()