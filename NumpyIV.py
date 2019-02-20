import numpy as np

a1 = np.array([1,2,3,4,5,6])
# first 2 numbers. in 0:2, 2 is exlusive
print(a1[0:2])

#second from the last - Reverse index
print(a1[-2])

a2 = np.arange(12).reshape(3,4)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 
[3 7]
'''
print(a2)
#0 to 1 - rows, 3 col
print(a2[0:2 , 3])

#the last row -[ 8  9 10 11]
print(a2[-1])

#last row, 0-2 cols - [ 8  9 10]
print(a2[-1,0:3])

print(a2)
#all rows, 2-3 cols
'''
[[ 2  3]
 [ 6  7]
 [10 11]]
'''
print(a2[:,2:4])

print(a2)
'''[0 1 2 3]
[4 5 6 7]
[ 8  9 10 11]'''
for eachrow in a2:
    print(eachrow)

a3 = a2 * 10
print(a3)

#verical stacking
'''
[[  0   1   2   3]
 [  4   5   6   7]
 [  8   9  10  11]
 [  0  10  20  30]
 [ 40  50  60  70]
 [ 80  90 100 110]]
'''
print(np.vstack((a2,a3)))

#horizontal stacking
'''
[[  0   1   2   3   0  10  20  30]
 [  4   5   6   7  40  50  60  70]
 [  8   9  10  11  80  90 100 110]]
'''
print(np.hstack((a2,a3)))

#horizontally split the arrays
'''
[[0 1]
 [4 5]
 [8 9]]
[[ 2  3]
 [ 6  7]
 [10 11]]
'''
horizontalSplit = np.hsplit(a2,2)

for i in horizontalSplit:
    print(i)


#vertically split the arrays
'''
[[0 1 2 3]]
[[4 5 6 7]]
[[ 8  9 10 11]]
'''
verticalSplit = np.vsplit(a2,a2.shape[0]) #a2.shape[0] - number of rows

for i in verticalSplit:
    print(i)

'''
[[False False False False]
 [False False  True  True]
 [ True  True  True  True]]
'''
print(a2)
b = a2 > 5
print(b)

''' [ 6  7  8  9 10 11]'''
print(a2[b])

a2[b] = -100
print(a2)






