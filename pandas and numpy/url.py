# csv file import from github
import pandas as pd
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df
# head  -> starting 5 rows
df.head(2)
# head -> 2 rows data
df.head(-3)
# head -> negative number