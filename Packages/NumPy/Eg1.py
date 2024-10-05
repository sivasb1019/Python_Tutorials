import numpy as np

# data1 = [10, 27, 0, 19, 30, 8, 12]
data1 = [[1,2,3,4],[5,6,7,8]]
arr1 = np.array([[1,2,3,4],[5,6,7,8]])
print("Array:",arr1)
print("Array Type:",arr1.dtype)
print("Array Shape:",arr1.shape)
print("Array Dimension:",arr1.ndim)
print("Array Item Size:",arr1.itemsize)
print("Array Size:",arr1.size)
print("Array Transverse:",arr1.T)
print("Array Flatten:",arr1.flatten())
print("Array Reshape:",arr1.reshape((4,2)))
