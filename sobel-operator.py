# -*- coding: utf-8 -*-
"""
Edge detection of a greyscale image using sobel operator.

@author: himanshu
"""
import itertools
import numpy as np
import scipy.misc as misc

def sobel_edge(image):
    image=np.pad(image,(1,1),mode='constant')
    edge_image=np.empty(image.shape)
    for (i,j) in itertools.product(range(1,image.shape[0]-1),range(1,image.shape[1]-1)):
        k=image[i-1:i+2,j-1:j+2]
        #Convolving in x direction
        kx=(-1*k[0,0])+(0*k[0,1])+(1*k[0,2])+(-2*k[1,0])+(0*k[1,1])+\
        (2*k[1,2])+(-1*k[2,0])+(0*k[2,1])+(1*k[2,2])
        #Convolving in y direction
        ky=(1*k[0,0])+(2*k[1,0])+(1*k[2,0])+(0*k[0,1])+(0*k[1,1])+\
        (0*k[2,1])+(-1*k[0,2])+(-2*k[1,2])+(-1*k[2,2])
        edge_image[i,j]=(kx**2+ky**2)**0.5
    return edge_image[1:-1,1:-1]    #return convolved image with padding removed
    
default_image = misc.lena()
save_as = "/home/user/edge_lena.png"
edge_image = sobel_edge(default_image)
misc.imsave(save_as, edge_image)