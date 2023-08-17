import numpy as np
arr=np.array([[2,3,4],[5,6,7]])
print("sum of the array",arr.sum())
print("maximum of the array", arr.max())
print("minimum of the array", arr.min())
print("minimum of the array in row",arr.min(axis=1))
print("maximum of the array in row",arr.max(axis=1))
print( arr.cumsum(axis=1))
print(np.average(arr))

