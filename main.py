import numpy as np

print(np.__version__)

#######################################################################################################################
# basics #
#######################################################################################################################
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

#######################################################################################################################
# indexing #
#######################################################################################################################
# chain indexing
print(array[0][0][0])

# multidimentional indexing
print(array[1,1,1])

# multidimentional indexing is faster

# string concatenation
word=array[0,0,0]+array[1,0,0]
print(word)

#######################################################################################################################
# slicing #
#######################################################################################################################
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

#######################################################################################################################
# scaler arithmetic #
#######################################################################################################################

array=np.array([1,2,3])

print(array+1)
print(array-2)
print(array*3)
print(array/4)
print(array**5)

# vectroized math functions
array=np.array([1.01,2.5,3.99])

print(np.sqrt(array))
print(np.round(array))
print(np.ceil(array))
print(np.pi)

# area of a cicle
radii=np.array([1,2,3])
print(np.pi*radii**2)

# element wise arithmetic
array1=np.array([1,2,3])
array2=np.array([4,5,6])

print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1/array2)
print(array1**array2)

# comparision operations
scores=np.array([91,55,100,73,82,64])

# returns a boolean array
print(scores==100)
print(scores>=60)

scores[scores<60]=0
print(scores)

#######################################################################################################################
# broadasting #
#######################################################################################################################

# Broadcasting allows numpy to perferm operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape
# rules
# the dimensions have the same size
# or
# one of the dimensions has a size of 1

# a(4*3) + b(1*3) = result(4*3)

array1=np.array([
    [1,2,3,4]
])

array2=np.array([
    [1],
    [2],
    [3],
    [4]
])

print(array1.shape)
print(array2.shape)

# braodcast is possible (1,4), (4,1)
print(array1*array2)

# we cannot broadcast for (2,4), (4,1)

#######################################################################################################################
# aggregate functions #
#######################################################################################################################

# summarise data and typically return a single value
array=np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
# pos of min val
print(np.argmin(array))
print(np.argmax(array))
# sum all columns
print(np.sum(array,axis=0))
# sum all rows
print(np.sum(array,axis=1))

#######################################################################################################################
# filtering #
#######################################################################################################################

