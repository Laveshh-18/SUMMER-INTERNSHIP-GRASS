#One hot encoding in machine learning
import pandas as pd
data={
    'Colors':['red','blue','green','red','blue']
}
df=pd.DataFrame(data)
print("Original data")
print(df)

#One hot encoding
encoded_df=pd.get_dummies(df,columns=['Colors'])
print("After one hot encoding")
print(encoded_df)

