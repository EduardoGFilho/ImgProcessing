# Image Processing Project

[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/EduardoGFilho/ImgProcessing/blob/main/README.md)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt-br.md://github.com/EduardoGFilho/ImgProcessing/blob/main/README.pt.md)

_Translated with DeepL_

## The project envisages two image filtering problems:
* 1) Enhancing the contrast of an image
* 2) Removing “salt & pepper” and “Gaussian” noise from images


## 1) Enhancing the contrast of an image
Follow the steps:
* a) Study the code below.

~~~Matlab
%taken from http://www.mathworks.com/help/images/filter-images-using-predefined-filters.html
I = imread('moon.tif');
h = fspecial('unsharp')
I2 = imfilter(I,h);
imshow(I), title('Original Image')
figure, imshow(I2), title('Filtered Image')
~~~

* b) Instead of the filter h above (obtained with fspecial), build yourself a filter that produces a similar result, with contrast enhancement, and enter the matrix that denotes this filter.
  * The implementation is in the repository, the matrix used was:
~~~Python
# passing 0.2 as a parameter to the function
def fspecialUnsharpen(alpha):
 h = np.array([[-alpha, alpha-1, -alpha],
 [alpha-1, alpha + 5, alpha-1],
 [-alpha, alpha-1, -alpha]])
 return (1/(alpha+1))*h
~~~

* c) Explain why your filter enhances contrast and put a filtered image in your report alongside the original. It could be “moon.tif” itself or another one.
  * The images are in the repository, in the “Sharpen” folder.
  * The matrix shown can be obtained from the sum of a unit impulse and a matrix, defined in such a way that its convolution with an image produces approximately the same result as applying the Laplacian operator to it. Based on the associative property of convolutions, we can understand a convolution of the image with the matrix defined as representing the sum of the image with the Laplacian itself. Since the Laplacian operator only has a value other than 0 when there is a variation in the intensity of a pixel in relation to its “neighborhood”, we can conclude that the result of the convolution will be an image composed of the original plus the value where there is a variation in its intensity, which is perceived as enhancement.
* d) Can your filter be understood as “low pass” or “high pass”?
  * As elaborated in the previous question, the filter emphasizes the regions of greatest intensity variation in the image, so it can be understood as “high-pass”.

## 2) Removing “salt & pepper” and “Gaussian” noise from images

Follow the steps:
* a) Take a photo that has a relatively homogeneous background (“almost” a single color) and one or more objects in the foreground. The minimum resolution is 200 x 200 pixels (can be higher). It can be a photo of yourself or a face taken from the Internet. Don't repeat the photo used by a colleague or let them repeat yours. To inspire you and serve as an example, the photo below has the desired characteristics.
  * The image is in the repository, in the "PSNR" folder.

* b) If the image is in color, convert it to grayscale, using 8 bits per pixel, with values from 0 to 255. The rgb2gray.m function does this. The grayscale image will be called “original_im”.
  * It's in the repository
* c) Using the imnoise function, create a noisy version of the original image with “salt & pepper” noise and a density (“density”, imnoise parameter) of 0.06. Repeat the step but with a density of only 0.005. In addition to these two images with salt & pepper noise, generate images with Gaussian noise of mean 0 and variances 0.001 and 0.03, for example, with the command:
~~~Matlab
imnoise(im_original,'gaussian',0,0.001)
~~~
In the end, you should have 4 noisy versions of the original image.


Your task is to use filters to reduce the noise of the noisy versions and compare them with the original image. The figure of merit of the filtering will be the PSNR, or “peak signal to noise ratio”, which uses the maximum value of a pixel as the “peak”, which in this case is 255. The PSNR can be calculated in dB as follows:
~~~Matlab
error=im_original-im_little_noise; %error image
MSE=mean(error(:).^2) %error(:) is a vector
PSNR = 10*log10(255^2/MSE) %value in dB
~~~

The two filters to be used are the mean and median. The average filter can be obtained with ``fspecial(‘average’,M)`` , where M indicates that the filter kernel is of dimension M x M. After obtaining the filter kernel, you can use the ``filter2`` function to perform the filtering. The median filter can directly use the ``medfilt2`` function with something like
``medfilt2(noisyImage,[M M])``
where the [M M] indicates a region of M x M pixels from which the median is extracted. For both filters, vary the values of M in the set {3, 5, 7}.

* d) For each of the 4 noisy versions, for each of the two filter types (mean and median) and for each of the 3 values of M, calculate the PSNR between the original image and the noisy image after passing through the filter. To get an idea of the values involved, also calculate the PSNR between the original image and the noisy version, without filtering.
  * In the repository.
At the end of the simulations, you will have results like the one below. Compose a table from them and place it as part of your report. Also include the Matlab / Octave script used.

Answer the following in the report:
* 1) Why is the median filter so much better than the mean filter for salt & pepper noise?
  * Since salt and pepper noise is characterized by completely black or completely white dots scattered throughout the image, represented by the maximum or minimum intensity value in a digital image, when organizing them in a list, the noisy pixels will always be at the ends of the list. Since the median of a list returns only the values in its middle, noisy pixels tend to be ignored by the algorithm. Furthermore, if the distribution of black and white pixels is similar in the same region, there will be little displacement of the pixels in the middle of the list since the number of white pixels added to one end and black pixels added to the other tends to balance out.
* 2) The PSNR is an objective figure of merit, but analyzing the images subjectively, which filter best preserves the edges of the objects in the image?
  * Analyzing subjectively, the median filter converts the edges of the objects better.

* 3) When the noise is Gaussian and the PSNR is relatively high, the filters don't seem to help much (improve the PSNR). But when the PSNR is low, they seem to improve it. Do you agree? If so, what is the reason for this behavior? If not, in which aspect is the reasoning incomplete?
  * I agree with the statement. The behavior is probably due to the fact that when an image already has low noise (high PSNR), no matter how much noise is removed, the difference caused by it will not be very significant, which is accentuated by the fact that dB is a logarithmic scale. On the other hand, when the image is noisy, any effect that the filter causes is likely to cause a reduction in noise, and therefore a more significant change in PSNR.
* 4) Thinking about the computational cost of filtering processes, which filter requires more processing power, the average or median?
  * The computational cost depends on the algorithms used, however, assuming efficient implementation of both filters, the most costly would be the median filter, as it requires operations such as sorting a list for each pixel in the image.
