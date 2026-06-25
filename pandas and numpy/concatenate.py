#concatenate
#1d
import numpy as np
arr1=np.array([10,20,30])
arr2=np.array([1,2,3])
arr1_arr2=np.concatenate((arr1,arr2))
print(arr1_arr2)
print(np.concatenate((arr1,arr2)))
print((arr1+arr2))


#2d
import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[4,8,5]])
arr1_arr2 = np.concatenate((arr1,arr2))
print(arr1_arr2)