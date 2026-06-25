import pandas as pd

d = {
    "name":["kunal","dheeraj","anjali","praveen","yash","danish"],
    "roll-no":[12,13,14,15,16,17]
}
df = pd.DataFrame(data=d)
print(df)