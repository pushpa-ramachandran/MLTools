import numpy as np

a1 = np.arange(15).reshape(3,5)
for eachCell in a1.flatten():
    print(eachCell)

a2 = np.arange(4).reshape(2,2)
#Fortran Order
'''
[[0 1]
 [2 3]]
0
2
1
3
'''
print(a2)
for i in np.nditer(a2,order='F'):
    print(i)

#C order - Same as flatten
'''
[[0 1]
 [2 3]]
0
1
2
3
'''
print(a2)
for i in np.nditer(a2,order='C'):
    print(i)

#[0 1 2 3]
for x in np.nditer(a2, order = 'C', flags = ['external_loop']):
    print(x)

'''
[0 2]
[1 3]
'''
for x in np.nditer(a2, order = 'F', flags = ['external_loop']):
    print(x)

'''
Read from an array and write to the same array
[[0 1]
 [4 9]]
'''
for x in np.nditer(a2, op_flags=['readwrite']):
    x[...] = x*x
print(a2)

a3 = a2 **2
print(a3)


'''
Iterate thru 2 arrays simultaneously - Arrays should be broadcastable
[[0 1]
 [4 9]]
 
[[ 0  1]
 [16 81]]
0 0
1 1
4 16
9 81
'''
for x,y in np.nditer([a2,a3]):
    print(x,y)
