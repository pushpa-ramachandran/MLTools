import numpy as np

# One dimensional - printed as rows - [0 1 2 3 4 5]
arr = np.arange(6)
print (arr)

#2 dimensional -
'''
the last axis is printed from left to right,
the second-to-last is printed from top to bottom,
the rest are also printed from top to bottom, with each slice separated from the next by an empty line

[[0 1 2]
 [3 4 5]]
'''
arr = np.arange(6).reshape(2,3)
print (arr)
'''
[[[ 0  1  2]
  [ 3  4  5]
  [ 6  7  8]
  [ 9 10 11]]

 [[12 13 14]
  [15 16 17]
  [18 19 20]
  [21 22 23]]]
'''
arr = np.arange(24).reshape(2,4,3)
print (arr)

#Basic Operations

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])

#add [ 6  8 10 12]
print(a1+a2)

#subtract [-4 -4 -4 -4]
print(a1-a2)

#To the Power [ 1  4  9 16]
print(a1 ** 2)

# multiple operations [ 84.14709848  90.92974268  14.11200081 -75.68024953]
print( 100 * np.sin(a1))

#Boolean [1 2 3 4] & [False False  True  True]
print(a1)
print(a1 > 2)

#elementwise product
'''
[1 2 3 4]
[5 6 7 8]
[ 5 12 21 32]
'''
print(a1)
print(a2)
print(a1 * a2)

#dot(matrix) product
'''
[1 2 3 4]
[5 6 7 8]
70
'''
print(a1)
print(a2)
print(a1 @ a2)

#dot(matrix) product
'''
[1 2 3 4]
[5 6 7 8]
70
'''
print(a1)
print(a2)
print(a1.dot(a2))

#+= and *=, act in place to modify an existing array rather than create a new one.
'''
[1 2 3 4]
[4 5 6 7]
'''
print(a1)
a1+=3
print(a1)

#need to be careful about automatic conversions
'''
[4 5 6 7]
[0. 1. 2. 3.]
[ 4.  6.  8. 10.]
'''
f1 = np.arange(4, dtype=float)
print(f1)
a1 = a1 + f1
print(a1)

