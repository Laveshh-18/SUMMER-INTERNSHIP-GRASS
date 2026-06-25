#2d array
import numpy as np
arr = np.arange(14).reshape(7,2)
print(arr)
up_arr=arr.reshape(2,7)
print(up_arr)
down_arr=up_arr.reshape(7,2)
print(down_arr)