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