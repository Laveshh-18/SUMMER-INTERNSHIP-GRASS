#pie chart
import matplotlib.pylab as plt
fruits=['apple','banana','orange','watermelon']
count=[40,30,15,70]
plt.pie(count,labels=fruits,startangle=90)
plt.show()