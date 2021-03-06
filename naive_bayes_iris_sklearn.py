# -*- coding: utf-8 -*-
"""naive_bayes_iris_sklearn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uS0yJBCqVglEtOOakSlp5yf9MNEC2vxM
"""

# load the iris dataset 
from sklearn.datasets import load_iris 
iris = load_iris() 
from   sklearn.metrics import  accuracy_score ,confusion_matrix

# store the feature matrix (X) and response vector (y) 
#iris
X = iris.data 
y = iris.target

# splitting X and y into training and testing sets 
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

# training the model on training set 
from sklearn.naive_bayes import GaussianNB 
gnb = GaussianNB() 
results=gnb.fit(X_train, y_train) 
results

# making predictions on the testing set 
y_pred = gnb.predict(X_test) 
y_pred

# comparing actual response values (y_test) with predicted response values (y_pred) 
from sklearn import metrics 
print(accuracy_score(y_test, y_pred)*100)

print(confusion_matrix(y_test, y_pred))