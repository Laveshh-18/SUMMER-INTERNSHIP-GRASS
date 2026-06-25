"""
#question on multibar 

import matplotlib.pylab as plt
import numpy as np
x=["group A","group B","group C","group D"]
y=[10,20,30,40,]
y2=[20,30,25,30]
w=0.40
plt.bar(x,y,label="boys")
plt.bar(x,y2,label="girls")
plt.xlabel('groups')
plt.ylabel('numbers of products')
plt.legend()
plt.show()
"""
import matplotlib.pyplot as plt
import numpy as np
groups = ['Group A', 'Group B', 'Group C', 'Group D']
girls = [10, 20, 20, 40]
boys = [20, 30, 25, 30]
x = np.arange(len(groups))
width = 0.4
plt.figure(figsize=(8, 5))
plt.bar(x - width/2, girls, width, label='Girls', color='tab:blue')
plt.bar(x + width/2, boys, width, label='Boys', color='tab:orange')
plt.xlabel('Groups')
plt.ylabel('Number of Students')
plt.title('Number of Students in each group')
plt.xticks(x, groups)
plt.legend()

for i, v in enumerate(girls):
    plt.text(x[i] - width/2, v + 0.5, str(v), ha='center')

for i, v in enumerate(boys):
    plt.text(x[i] + width/2, v + 0.5, str(v), ha='center')

plt.tight_layout()
plt.show()





