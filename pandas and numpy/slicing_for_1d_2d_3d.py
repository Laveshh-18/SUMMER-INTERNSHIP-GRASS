#slicing for id
import numpy as np
arr = np.arange(11)
print(arr)
up_arr = arr[:3]
print(up_arr)

print("-----------------------------")
#slicing for 2d
arr = np.arange(14).reshape(7,2)
print(arr)
up_arr=arr[:3,:]
print(up_arr)

print("-----------------------------")

#slicing for 3d
arr = np.arange(27).reshape(3,3,3)
print(arr)
up_arr=arr[:2,:,:]
print(up_arr)