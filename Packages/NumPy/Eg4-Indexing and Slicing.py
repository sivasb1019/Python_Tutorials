import numpy as np

arr = np.arange(10)
print("Array:",arr)
print("\nArray[1:3]:",arr[1:3])
arr[0:3] = 10
print("\nReplacing Array values[0:3] to 10:",arr)
print("\nArray[2]:",arr[2])
arr_slice = arr[5:8]
print("\nSLiced Array[5:8]:",arr_slice)
print("\nArray:",arr)
arr_slice[1]= 10
print("\nReplacing Sliced Array[1] to 10:",arr_slice)
print("\nArray:",arr)

# useful in deep learning

arr = np.linspace(1, 10, 15)
print("\n",arr)
