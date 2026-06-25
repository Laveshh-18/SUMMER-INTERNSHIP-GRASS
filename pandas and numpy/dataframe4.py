import pandas as pd 
data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000, 52000],
    "Experience": [2, 3, 5, 4, 1, 3]
}

DF1=pd.DataFrame(data)
print(DF1)

# 1. head()
print("head ")
print(DF1.head())
print("\n")
print(DF1.head(6))
print("\n")
print(DF1.head(-3))

# tail()
print("\n tail")
print(DF1.tail())
print("\n")
print(DF1.tail(3))
print("\n")
print(DF1.tail(-4))

# describe 
print(DF1.describe())

# info 
print(DF1.info())