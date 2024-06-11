import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as LinearR

df = pd.read_csv("C:\Codes\Machine Learning\course1\I.P files\homeprices.csv")

plt.xlabel(' Area(sqr ft.) ')
plt.ylabel(' Price(INR)')
plt.scatter(df.Area, df.Price, color= "red", marker = "+")

reg  = LinearR()
reg.fit(df[['Area']], df.Price)
LinearR()

reg.predict([[3300]])