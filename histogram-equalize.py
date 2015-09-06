# -*- coding: utf-8 -*-
"""
Implementing histogram equalizer in python.
Histogram of an image with poor contrast has most of its intensity levels very 
closely spaced in a small area. To improve contrast replace intensity values 
with their corrosponding cmf values. This relults in a very well distributed histogram.
This method works well with images having backgrounds and foregrounds that are 
both bright or both dark.
@author: himanshu
"""

import scipy.misc as misc
import numpy as np
import itertools
import matplotlib.pyplot as plt


class HistogramEqualize():
    def __init__(self):
        pass
    
    def get_pdf(self,image, depth):
        """Returns UNNORMALIZED probability mass function of the image.
        depth = bits per pixels"""
        pdf = np.zeros((2**depth), dtype=int)
        for (i,j) in itertools.product(range(0,image.shape[0]), range(0,image.shape[1])):
            pdf[image[i,j]] = pdf[image[i,j]] + 1
        return pdf
        
    def get_cdf(self, pdf):
        """Returns UNNORMALIZED cumulative density function of the given p.m.f
        depth = bits per pixels"""
        cdf=np.zeros((pdf.shape[0]), dtype=int)
        cdf[0]=pdf[0]        
        for i in range(1,pdf.shape[0]):
            cdf[i] = cdf[i-1] + pdf[i]
        return cdf
        
    def equalize(self, image,depth):
        """Returns as equalized image with intensity levels in image replaced 
        by its corrosponding cdf values"""
        eq_image=np.empty(image.shape)
        pdf=self.get_pdf(image, depth)
        cdf=self.get_cdf(pdf)/(image.shape[0]*image.shape[1])
        for (i,j) in itertools.product(range(0,image.shape[0]), range(0,image.shape[1])):
            eq_image[i,j]=int(cdf[image[i,j]]*(2**depth-1))
        return eq_image
   
"""Equalizing Lena
depth=8 bpp"""
default_image=misc.lena()
save_as="/home/user/equalized.png"
equalizer=HistogramEqualize()
eq_image=equalizer.equalize(default_image, depth=8)
misc.imsave(save_as, eq_image)

"""Plots of histograms"""
plt.figure(1)
plt.subplot(2,1,1)
plt.hist(default_image.flatten(), bins=40,  normed=True)
plt.ylabel('Probability')
plt.title('Unequalized Histogram')
plt.show()
plt.subplot(2,1,2)
plt.hist(eq_image.flatten(), bins=40, color='r', normed=True)
plt.ylabel('Probability')
plt.title('Equalized Histogram')
plt.show()