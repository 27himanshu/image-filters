# -*- coding: utf-8 -*-
"""
Scaling of greyscale images using linear interpolation.
@author: himanshu
"""
import numpy as np
import scipy.misc as misc


default_image = misc.lena()
save_as = "/home/user/lena-scaled.png"


class Scale():

    """ Linear scaling of image 'k' times. (k>1)
        k should be an integer."""

    def __init__(self, k):
        self.k = k
        return

    def scale_row(self, image):
        """Linear scaling of all the rows of image.
        An example of scaling of row is:
            k=3
            input = [[15, 30, 15],
                    [30, 15, 30]]
            scaled_output =
                    [[15, 20, 25, 30, 25, 20, 15],
                     [30, 25, 20, 15, 20, 25, 30]]
            (k-1) elements are inserted between each of two elements of every
            row"""
        scaled_image = np.empty( (image.shape[0], (self.k*image.shape[1] -\
        self.k+1)), dtype=int )
        row_number = 0
        for a_row in image:
            for i in (range(len(a_row)-1)):
                delta = ((a_row[i+1] - a_row[i])/self.k)
                scaled_image[row_number][self.k * i:self.k * i + self.k + 1] =\
                [ (a_row[i] + j * delta) for j in range( self.k + 1)]
            row_number = row_number+1
        return scaled_image

    def scale_column(self, image):
        """Linear scaling of all the columns of the image.
        An example of scaling of columns is:
            k=3
            input = [[15, 30, 15],
                     [30, 15, 30]]
            scaled_output =
                    [[15, 30, 15],
                     [20, 25, 20],
                     [25, 20, 25]
                     [30, 15, 30]]"""
        image = image.T #Taking transpose and then doing row scaling is equivalent to column scaling
        scaled_image = self.scale_row(image)
        return scaled_image.T

"""Scaling Lena by a factor k = 2"""
scale = Scale(2)
scaled_image = scale.scale_column(scale.scale_row(default_image))
misc.imsave(save_as, scaled_image)