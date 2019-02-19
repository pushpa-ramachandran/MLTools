import numpy as np

'''
[ 0  1  2  3  4  5  6  7  8  9 10 11]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[ 0  1  2  3  4  5  6  7  8  9 10 11]
'''
a1 = np.arange(12)
print(a1)
#reshaping and assigning to a new variable. a1 remains unchanged
b1 = a1.reshape(3,4)
print(b1)

print('b1 \n' ,b1)

#ravel() flattens the array
'''
 flattened b1 
 [ 0  1  2  3  4  5  6  7  8  9 10 11]
'''
c1 = b1.ravel()
print(' flattened b1 \n' ,c1)

'''
Max - 11
Min - 0
Sum - 66
'''
print('Max -' ,b1.max())
print('Min -' ,b1.min())
print('Sum -' ,b1.sum())

'''
b1 -
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
axis=0 [12 15 18 21]
'''
print('b1 -\n' ,b1)
print('axis=0', b1.sum(axis=0))

'''
b1 -
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
axis=1 [ 6 22 38]
'''
print('b1 -\n' ,b1)
print('axis=1', b1.sum(axis=1))

'''
[[0.         1.         1.41421356 1.73205081]
 [2.         2.23606798 2.44948974 2.64575131]
 [2.82842712 3.         3.16227766 3.31662479]]
'''
print(np.sqrt(b1))

#3.452052529534663
print(np.std(b1))


