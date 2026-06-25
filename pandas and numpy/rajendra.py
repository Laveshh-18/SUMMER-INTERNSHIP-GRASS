import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df["marks"] = df["marks"].fillna(100)
df["roll no"] = df["roll no"].fillna(200)
 
print(df)