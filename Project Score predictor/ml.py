import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error



#cleaning data
df = pd.read_csv(r"C:\Users\newto\OneDrive\Desktop\Summer internship\Grass\Project Score predictor\archive\IPL.csv", index_col = None)
df = df[df["innings"]==1]
df = df[df["team_balls"] > 36]
df["score"] = df.groupby("match_id")["runs_total"].transform("sum")
match_ids = df["match_id"].unique()
print("Data cleaned")


# preparing data sets for training and testing data
mId_train , mId_test =train_test_split(match_ids , test_size = 0.2 )
X = df[['match_id','team_runs', 'team_balls', 'team_wicket', 'batter_runs', 'batter_balls','venue']]
y = df[["match_id","score"]]
X = pd.get_dummies(X, columns=["venue"])
X_train = X[X["match_id"].isin(mId_train)].drop("match_id",axis = 1) #dropped match_id becouse its useless
X_test = X[X["match_id"].isin(mId_test)].drop("match_id", axis =1)
y_train = y[y["match_id"].isin(mId_train)].drop("match_id", axis =1)
y_test = y[y["match_id"].isin(mId_test)].drop("match_id",axis =1 )
print("data splitted")

# Here I choosed to Match-wise split becouse:
# Each IPL match contains multiple ball-by-ball records. Randomly splitting
# rows would place balls from the same match in both training and testing,
# leading to overly optimistic performance. Splitting by match_id ensures
# the model is evaluated only on completely unseen matches.



#training the regression model
model = LinearRegression()
model.fit(X_train , y_train)
pred = model.predict(X_test)
print("model trained")


#calculating the error
error = mean_absolute_error(y_test,pred)
print(error) #error turned out to be approx 14 runs per predection

#saving the model
joblib.dump(model,"IPL_SCORE_PREDICTOR.pkl")

#plotting ideal regression
plt.scatter(y_test, pred , color = 'pink')
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red"
)
plt.savefig("plot/idealRegression.png")