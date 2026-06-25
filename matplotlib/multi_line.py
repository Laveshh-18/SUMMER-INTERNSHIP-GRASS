#multiple line chart
import matplotlib.pylab as plt
x=[2010,2015,2020,2025]
y1=[100,200,260,290]
y2=[150,185,195,300]
plt.plot(x,y1,label='jeans')
plt.plot(x,y2,label='shirt')
plt.legend()  #info of label
plt.show()
