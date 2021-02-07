from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import pandas as pd
import numpy as np

df = pd.read_csv("cocktail_observations.csv")
y = df.pop('cocktails')
X = df

svc = SVC()
param_grid ={'C': [0.01, 0.1, 1, 10, 100],
    'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(svc, param_grid=param_grid, cv=2, iid='True')
grid.fit(X, y)

X_test = #JSON file

rankings = grid.decision_function(X_test)

tail_index=[]
for i in range(rankings.shape[1]):
    tail_index.append(np.argmax(rankings))
    rankings[0][np.argmax(rankings)] = np.min(rankings)-1