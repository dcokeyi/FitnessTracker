
## importing libraries
import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import sklearn.metrics


#retrieving path
dataset=pd.read_csv('data/CardioGoodFitness.csv') 
#transform categorical data
le_Gender = LabelEncoder()

dataset['Gender'] = le_Gender.fit_transform(dataset['Gender'])

variables = ['Age', 'Gender', 'Usage', 'Miles']

"""**Choosing a model and training**"""
X = dataset[variables]
sc = StandardScaler()
X = sc.fit_transform(X)
Y = dataset['Fitness']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

#train model
regressor = ExtraTreesRegressor(n_estimators = 200)
regressor.fit(X_train,y_train)

#prediction and evaluation
y_train_pred = regressor.predict(X_train)
y_test_pred = regressor.predict(X_test)


print("Test RMSE: ", np.sqrt(sklearn.metrics.mean_squared_error(y_test, y_test_pred)))




def absoluteError():
    return sklearn.metrics.mean_absolute_error(y_test, y_test_pred)

def squaredError():
    return np.sqrt(sklearn.metrics.mean_squared_error(y_test, y_test_pred))


def search(Age, Gender,Usage,Miles):
    print('Predicting on new data\n\n')
    person = [float(Age),Gender,float(Usage),float(Miles)]
    print('Billy - ',str(person))



    person[1] = le_Gender.transform([person[1]])[0] 
    

    X = sc.transform([person])

    fitness = regressor.predict(X)[0]
    

    return fitness

