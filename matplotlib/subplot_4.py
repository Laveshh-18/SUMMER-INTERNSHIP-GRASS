import matplotlib.pyplot as plt
 
# subplot
# first chart
x = [1,2,3,4,5]
y = [10,20,30,40,55]
 
plt.subplot(2,2,1) # row,cols,position
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
 
# second chart
x1 = ['apple','banana','orange','watermelon']
y1 = [40,30,15,70]
 
plt.subplot(2,2,2) # row,cols, position
plt.pie(y1,labels=x1,startangle=90)
plt.xlabel("x1 axis")
plt.ylabel("y1 axis")
 
# third chart
x = [1,2,3,4,5]
y = [10,20,30,40,55]
 
plt.subplot(2,2,3) # row,cols,position
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
# fourth chart
x1 = ['apple','banana','orange','watermelon']
y1 = [40,30,15,70]
 
plt.subplot(2,2,4) # row,cols, position
plt.pie(y1,labels=x1,startangle=90)
plt.xlabel("x1 axis")
plt.ylabel("y1 axis")
 
 
plt.tight_layout()
plt.show()