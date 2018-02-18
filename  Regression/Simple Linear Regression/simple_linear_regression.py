import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Salary_Data.csv")
X = df.iloc[:, :-1].values
y = df.iloc[:, 1].values


from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3)

# fitting Simple Linear Regression to the training data

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train, y_train)

# predicting the Test set result

y_pred = regressor.predict(X_test)

# visualizing training set result

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train))
plt.title("Salary vs. Exprience (Training set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# visualizing test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train))
plt.title("Salary vs. Exprience (Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
