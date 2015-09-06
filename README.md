# Image Filters
Implementation of some basic image processing filters in python.  
The following python libraries are used:  
1. Numpy
2. Scipy


##Linear Scaling
An image is scaled first row-wise then colum-wise or vice-versa.  

        """Linear scaling of all the rows of an image.
        An example of scaling of row is:
            k=3
            input = [[15, 30, 15],
                    [30, 15, 30]]
            scaled_output =
                    [[15, 20, 25, 30, 25, 20, 15],
                     [30, 25, 20, 15, 20, 25, 30]]
            (k-1) elements are inserted between each of two elements of every
            row"""  
In linear scaling we add a number of points between two points such that the points added lies on the line joining the two original points.  


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
                     
#### Input image (512x512)
![Input image] (http://i.imgur.com/vOXyzGG.png)
#### Output image scaled by the factor of 2 (1023x1023) 
![Output image] (http://i.imgur.com/iKYA4iB.png)

## Median Filter

An n x n kernel is convolved with image.  
Each pixel of the image is replaced by the median value of the kernel. It is effective in reducing salt-pepper noise.  
For example consider the following 2D matrix 


			"""[[12, 15, 9],  
				[3, 5, 10],  
				[7, 8, 11]]"""    


In this matrix the middle value 5 is replaced by the median of all the elements of the matrix i.e. 9

#### Input Image
![Input] (http://i.imgur.com/GfF9JTa.png)

#### Output Image after convolving with a median filter of shape 3 x 3
![output] (http://i.imgur.com/6VYIIqS.png)


##Sobel Operator


A 3 x 3 vector that when convolved with image gives an extimate of gradient in either x-direction or y-direction.  


			"""Gx = [[-1, 0, 1],  
					[-2, 0, 2],  
					[-1, 0, 1]]""" 
				
			"""Gy = [[-1, -2, -1],  
					[0, 0, 0],  
					[1, 2, 1]]"""
				
When Gx is convolved with the image it gives approximate gradient in x direction and when Gy is convolved with image it approximates gradient in y-direction.

### Input Image  
![Input image](http://i.imgur.com/vOXyzGG.png)


### Output Image  
![Output image](http://i.imgur.com/bbB2WqF.png)  


##Histogram Equalization  
Histogram of an image with poor contrast has most of its intensity levels very closely spaced in a small area. To improve contrast replace intensity values with their corrosponding cmf values. This relults in a very well distributed histogram. This method works well with images having backgrounds and foregrounds that are both bright or both dark.

### Input Image  
![Input image](http://i.imgur.com/vOXyzGG.png)


### Output Equalized Image  
![Output image] (http://i.imgur.com/kW87ggW.png)  
### Histograms of both images  
![Histograms] (http://i.imgur.com/aPRzvoq.png)
