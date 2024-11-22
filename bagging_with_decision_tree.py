# -*- coding: utf-8 -*-
"""bagging with decision tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18N2RjkKPWC039-6XXM3S34xuHNIb7-0r
"""

# bagging with decision tree
# import neccessiory libraies
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# synthetic data
X,y = make_classification(
    n_samples=1000,
    n_features=20,
    random_state=3
)
print(X,y)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=20)

# intialize the dececison tree claasifier
base_estimator = DecisionTreeClassifier(random_state=20)


# initialize the bagging classifier
bagging_model = BaggingClassifier(
    estimator = base_estimator,
    n_estimators = 15,
    random_state = 20         # numbers of trees
)

# train the bagging classifier
bagging_model.fit(X_train,y_train)

# make prediction
y_pred = bagging_model.predict(X_test)

# evalute model
accuracy = accuracy_score(y_test,y_pred)
print(f"accuracy: {accuracy}")