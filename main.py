import numpy as np

print(np.__version__)

# to create the numpy array
array=np.array([1,2,3,4])
print(array)
print(type(array))

# if you do this normal python list the array will repeat itself
# but in numpy if doubles every no
array=array*2
print(array)

# to check the no of dimention
# 0
array=np.array('A')
print(array.ndim)

# 1
array=np.array(['A','B','C'])
print(array.ndim)

# 2
array=np.array([['A','B','C'],
               ['D','E','F']])
print(array.ndim)

# 3
array=np.array([
    [['A','B','C'],['D','E','F']],
    [['G','H','I'],['J','K','L']]
])
print(array.ndim)

# (depth, no of rows, no of columns)
print(array.shape)

# chain indexing
print(array[0][0][0])

# multidimentional indexing
print(array[1,1,1])

# multidimentional indexing is faster

# string concatenation
word=array[0,0,0]+array[1,0,0]
print(word)

# slicing
array=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

# array[start:end:step]
# end is exlusive
# step is 1 by default
print(array[0:3])

# start from 1 till the end
print(array[1:])

# select all with step 2
print(array[::2])

# reverse
print(array[::-1])

# column selection
# select all row and column 0
print(array[:, 0])

# select all row with column 2 from the end
print(array[:,-2])

# print all 3 columns
print(array[:,0:3])

# every second column
print(array[:,::2])

# selecting row and column
print(array[0:2,0:2])