"""#subplot
#first chart
import matplotlib.pylab as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel(" y axis")
plt.subplot(1,2,1)#row , col,position
plt.show()

#second chart
x1=['apple','banana','orange','watermelon']
y1=[40,30,15,70]
plt.pie(y1,labels=x1)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()
"""

import matplotlib.pyplot as plt
 
# subplot
# first chart
x = [1,2,3,4,5]
y = [10,20,30,40,55]
 
plt.subplot(1,2,1) # row,cols,position
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
 
# second chart
x1 = ['apple','banana','orange','watermelon']
y1 = [40,30,15,70]
 
plt.subplot(1,2,2) # row,cols, position
plt.pie(y1,labels=x1,startangle=90)
plt.xlabel("x1 axis")
plt.ylabel("y1 axis")
plt.tight_layout()
plt.show()
 

