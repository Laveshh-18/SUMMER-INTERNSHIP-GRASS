#data preprocessing
"""
import pandas as pd
data={
    'Name': ['Ram','Kamal','Ajay'],
    'Age':[25,None,32],
    'Salary':[5000,6000,None]
}
df=pd.DataFrame(data)
print("Original Dataframe")
print(df)

#null findout ,fillna, dropna
"""


import pandas as pd
data = {
    'Name': ['Ram', 'Kamal', 'Ajay'],
    'Age': [25, None, 32],
    'Salary': [5000, 6000, None]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# Find null values
print("\nNull Values:")
print(df.isnull().sum())

# Fill null values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean(),)

print("\nAfter fillna:")
print(df)

# Filter data
print("\nEmployees with Salary > 5500")
print(df[df['Salary'] > 5500])

print("\nEmployees with Age > 26")
print(df[df['Age'] > 26])

# Drop null values example
print("\nUsing dropna on original data:")
print(pd.DataFrame(data).dropna())