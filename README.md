# image-filters
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
                     
