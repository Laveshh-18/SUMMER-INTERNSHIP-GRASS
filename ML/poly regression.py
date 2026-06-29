import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
X = 4*np.random.rand(100, 1) -2
y = 4 + 5*X**2  + np.random.randn(100,1)
plt.scatter(X,y)
poly_features = PolynomialFeatures(degree = 2)
polyX = poly_features.fit_transform(X)
X_vals  = np.linspace(-2,2,100).reshape(-1,1)
polyX_vals = poly_features.fit_transform(X_vals)
reg = LinearRegression()
reg.fit(polyX,y)
pred = reg.predict(polyX_vals)
plt.scatter(X,y)
plt.plot(X_vals,pred,color="red")