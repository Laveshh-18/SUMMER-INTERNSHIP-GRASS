import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data="https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"
#data frame
df=pd.read_csv(data)
print(df)

#Standard Scalar
scalar=StandardScaler()
df['experience']=scalar.fit_transform(df[['experience']]) #2d
print(df)


#split data
x=df[['experience']]
y=df['salary']
print(x)
print(y)
"""
#line chart
plt.plot(data["experience"], data["salary"], marker='o', linewidth=2)
plt.title("Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()"""


# train test split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
print("x train: ",x_train)
print("x test: ",x_test)
print("y train: ", y_train)
print("y test: ", y_test)


# simple linear reg | prediction
from sklearn.linear_model import LinearRegression
 
# model fit
model = LinearRegression()
model.fit(x_train,y_train) # 2d
 
# input from user
user = int(input("Enter your Experience: "))
# model prediction
 
new_data = {
    "experience":[user]
}
 
df1 = pd.DataFrame(new_data)
print(df1)
pred_data = model.predict(df1)
print(pred_data[0])
 
 
"""
#model fit
model=LinearRegression()
model.fit(x_train,y_train)

#input from user
user=int(input("Enter from user:"))


#model prediction
new_data={
    "experience":[user]
}
df1=pd.DataFrame(new_data)
print(df1)
pred_data=model.predict(df1)
print(pred_data)
"""

