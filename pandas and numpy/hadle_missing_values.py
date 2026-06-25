import pandas as pd
import numpy as np
data={
    "Colors":["red","green","blue","orange","green","blue",np.nan]
}
df=pd.DataFrame(data)
#print(df)
#handle missing values
df.dropna(inplace=True)
print(df)


#Label encoding
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Colors_encoder']=le.fit_transform(df['Colors'])
print(df)
#OR
df['Colors_encoder']=LabelEncoder().fit_transform(df['Colors'])
print(df)


"""
one hot encoder
from sklearn.preprocessing import OneHotEncoder
print(df)
df.drop(df[['Colors_encoder','Colors_encoder1','Colors_encoder2','Colors_encoder3']],axis=1,inplace=True)
print(df)"""
