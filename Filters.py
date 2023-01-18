# %%
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
    return (np.ones((M, M)))/(M**2)


# %%
def isEven(x):
    return not (x%2)

def median_filter(img, filter_size):
    if(isEven(filter_size)):
        raise ValueError('I didn\'t want to deal with even sized "kernels"')
        
    img = np.array(img)
    img_final = img
    indexer = filter_size // 2
    inside_bounds = True
    a = 2

    for img_column in range(img.shape[0]):
        for img_row in range(img.shape[1]):
            tmp = []

            for filter_column in range(filter_size):
                
                i = img_column + filter_column - indexer

                if i >=0 and i < img.shape[0]:
                    for filter_row in range(filter_size):

                        j = img_row + filter_row - indexer
                        
                        if j >= 0 and j < img.shape[1] :
                            tmp.append(img[i][j])

            if(isEven(len(tmp))):
                #typecasting avoids overflow for even-sized list and white pixels
                #but since this is slow, it should only be done if need be
                img_final[img_column][img_row] = median(np.array(tmp, dtype=np.int16))
            else:
                tmp.sort()
                img_final[img_column][img_row] = tmp[len(tmp)//2]
            
            
    return img_final

#%%
def fspecialUnsharpen(alpha):
    h = np.array([[-alpha, alpha-1, -alpha],
                [alpha-1, alpha + 5, alpha-1],
                [-alpha, alpha-1, -alpha]])
    return (1/(alpha+1))*h