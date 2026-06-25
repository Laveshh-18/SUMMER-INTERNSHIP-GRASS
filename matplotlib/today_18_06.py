# subplots 2d
import matplotlib.pyplot as plt
# graph 1
year = [2010,2015,2020,2025]
dairy = [100,520,630,400]
 
# graph 2
farming = [300,200,250,100]
 
# graph 3
college = [10,20,25,30]
 
# graph 4
transport = [50,75,100,150]
 
 
fig,aux = plt.subplots(2,2) # 4 cols
# first row and first cols
aux[0][0].plot(year,dairy)
aux[0][0].set_xlabel("year")
aux[0][0].set_ylabel("dairy")
aux[0][0].set_title("dairy production")
 
aux[0][1].bar(year,farming)
aux[0][1].set_xlabel("year")
aux[0][1].set_ylabel("farming")
aux[0][1].set_title("farming production")
 
aux[1][0].pie(year,labels=college)
aux[1][0].set_xlabel("year")
aux[1][0].set_ylabel("college")
aux[1][0].set_title("college production")
 
aux[1][1].scatter(year,transport)
aux[1][1].set_xlabel("year")
aux[1][1].set_ylabel("transport")
aux[1][1].set_title("transport production")
 
 
plt.tight_layout()
 
plt.show()
 
 