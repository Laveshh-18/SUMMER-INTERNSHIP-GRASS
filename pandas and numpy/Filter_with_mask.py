#Filter with mask
#1d
import numpy as np
arr=np.array([12,24,24,45,67])
print(arr)
arr_f=arr[arr<40]
print(arr_f)
print("____________________")



import numpy as np
arr=np.array([12,50,30,24,45,67])
print(arr)
arr_f=arr[arr%2==0]
print(arr_f)

print("_____________________-")
#where keyword is used for filter the condition
#fancy indexing
import numpy as np
arr = np.array([10,20,30,40,50])
print(arr)
arr_fancy = arr[[0,2,4]] # 0 index value , 2 , 4 index value
print(arr_fancy)
 

print("______________________")


#np where
import numpy as np
arr1 = np.array ([[12,234,3,53],
                 [34,6,78,25]])
print(arr1)
print("-------")
arr_wa= np.where(arr1%2==0, "true", "false")
print(arr_wa)