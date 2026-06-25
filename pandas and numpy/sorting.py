#sorting in python
import numpy as np
arr = np.array([[5,60,20],[40,90,4]])
print(arr)
arr_s=np.sort(arr , axis=0)
print(arr_s)

#by default sorting is done in ascending order

#sorting for 2d array
print("________________________")
# sort 2d
import numpy as np
arr=np.array([[5,60,-2],[3,4,1]])
print(arr)
sort_arr=np.sort(arr)
print(sort_arr)

print("____________________________")
 
# descending sort
import numpy as np
arr= np.array([45,12,78,23,46])
print(arr)
descen_arr=np.sort(arr)[::-1]
print(descen_arr)
 