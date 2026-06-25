# while loop for 3d
import numpy as np
arr = np.arange(24).reshape(2, 3, 4)
 
 
i = 0
while i < len(arr):
  j = 0
  while j < len(arr[i]):
    k = 0
    while k < len(arr[i][j]):
      print(arr[i][j][k], end=" ")
      k += 1
    print()
    j += 1
  print()
  i += 1




  #while loop for 2d
import numpy as np
arr = np.arange(12).reshape(3, 4)
i = 0
while i < len(arr):
    j = 0
    while j < len(arr[i]):
        print(arr[i][j], end=" ")
        j += 1
    print()
    i += 1




#for loop for 3d
import numpy as np
arr = np.arange(24).reshape(2, 3, 4)
for i in arr:
    for j in i:
        for k in j:
            print(k, end=" ")
        print()
    print()