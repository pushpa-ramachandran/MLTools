# NumPy - Main object is the homogeneous multi dimensional array

import numpy as np

a = np.array([
    [ [1,2,3],  [1, 2, 3], [1, 2, 3]],
    [ [1,2,3],  [1, 2, 3], [1, 2, 3]]
])

#the number of axes (dimensions) of the array. - 3
print(a.ndim)

'''the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension.
 For a matrix with n rows and m columns, shape will be (n,m). 
 The length of the shape tuple is therefore the number of axes, ndim - (2,3,3)'''
print(a.shape)

#the total number of elements of the array. This is equal to the product of the elements of shape -18
print(a.size)

#an object describing the type of the elements in the array-int32
print(a.dtype)

#the size in bytes of each element of the array-4
print(a.itemsize)

#type of the class - <class 'numpy.ndarray'>
print(type(a))

#Array Creation
#array transforms sequences of sequences into
#two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on
#[[1. 2. 3.]
#[4. 5. 6.]]

b= np.array([(1,2.0,3),(4,5.0,6)])
print(b)

''' The function zeros creates an array full of zeros
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''
print(np.zeros((3,4)))

''' The function ones creates an array full of ones
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
'''
print(np.ones((3,4), dtype=int))


''' the function empty creates an array whose initial content is random and depends on the state of the memory. 
[[207   0   0   0]
 [  0   0   0   0]
 [  0   0 184   0]
 [  0   0   0   0]]
'''
print(np.empty((4,4), dtype=int))

'''
To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists
[1 5 9]
'''
print ( np.arange(1,10,4))


'''
 the function linspace that receives as an argument the number of elements that we want, instead of the step:
 [ 1.  4.  7. 10.]
'''
print ( np.linspace(1,10,4)) #4 numbers from 1 to 10

#creates a single dimensional array of 1000 elements
print((np.arange(1000)))

#creates a two dimensional array of 1000 elements with 200 rows and 5 cols
print(np.arange(1000).reshape(200,5))

