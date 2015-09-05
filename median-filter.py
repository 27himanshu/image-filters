# -*- coding: utf-8 -*-
"""
An n x n median filter.
Using this filter to resore an image corrupted with salt-pepper noise.
@author: himanshu
"""

import itertools
import numpy as np
import scipy.misc as misc

class Median():
    """An n x n Median filter.
    n must be an odd number."""
    
    def __init__(self, n):
        if(n%2 == 0):   #if n is not odd, taking n to be next odd number
            n = n + 1
        self.n = n
        self.delta = int(n - (n+1)/2)
        
    def pad(self, image, k = None):
        """Padding image
        Where 'k' is the number of additional rows and column added.
        If k is not provided then chosing appropriate value of k according to
        shape of median filter."""
        
        self.k = k
        if (self.k == None):
            self.k = self.delta
        return np.pad(image, (1, self.k), mode = 'constant')
        
    def convolve(self, image):
        """Convolving kernel with the image.
        Kernel is of order n x n.
        convolved_image is returned as output."""
        
        convolved_image=np.empty(image.shape)
        np.copyto(convolved_image, image)
        for (i,j) in itertools.product(range(self.delta, image.shape[0] - self.delta),\
        range(self.delta, image.shape[1] - self.delta)):    #using cross product of rows and columns to access each and every pixel (An alternative to nested for-loop)
            kernel = image[i-self.delta:i+self.delta+1, j-self.delta:j+self.delta+1]
            temp=list()
            for k in range(self.n):
                temp.extend(kernel[k])
            temp.sort()
            convolved_image[i,j]=temp[int((self.n*self.n)/2)]
        return convolved_image[self.delta:convolved_image.shape[0] - self.delta,\
        self.delta:convolved_image.shape[1] - self.delta]   #returned convolved image with padding removed
        
        
"Using a 3x3 median filter to remove salt-pepper noise"

default_image = "/home/user/salt.png"
save_as = "/home/user/restored.png"
image = misc.imread(default_image)
filter = Median(3)
restored_image = filter.convolve(filter.pad(image))
misc.imsave(save_as,restored_image)