#example of ravel 3d
import numpy as np
arr = np.arange(27).reshape(3,3,3)
print(arr)
#up_arr=arr.flatten()
#print(up_arr)
up_arr=arr.T
print(up_arr)
