# -*- coding: utf-8 -*-
"""logistic regression on iris dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EC4L9O8KgV_ZsrraERS9oH8DyomCsxQ4
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
df = pd.read_csv("/content/Iris.csv")
#print(df.head)
x=df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
y=df["Species"]

#print(x,y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)
print(x_train)
print(y_test)
print(y_train)
print(y_test)

# import the class
from sklearn.linear_model import LogisticRegression

# instantine the model(using  the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(x_train,y_train) # 75% data for analysis

# predict the data
y_pred=logreg.predict(x_test) # 25% of data is used for testing
#print(y_pred)

# import the metrics class
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
print(cnf_matrix)

# import required modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

class_names= [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)
#print
# create headmap
sns.heatmap(pd.DataFrame(cnf_matrix),annot=True,cmap="Greens",fmt="d",annot_kws={"size":10})
ax.xaxis.set_label_position("bottom")
plt.tight_layout()
plt.title("confusion matrix", y=1.4)
plt.xlabel('actual label')
plt.xlabel('predicated labels')
# plt.show

print("accuracy of the model:",metrics.accuracy_score(y_test,y_pred))
#print("precision of the model:",metrics.precision_score(y_test,y_pred))

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
df = pd.read_csv("/content/Iris.csv")
#print(df.head)
x=df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
y=df["Species"]

#print(x,y)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)
# print(x_train)
# print(y_test)
# print(y_train)
# print(y_test)

# import the class
from sklearn.neighbors import KNeighborsClassifier

# instantine the model(using  the default parameters)
knn = KNeighborsClassifier()

# fit the model with data
knn.fit(x_train,y_train) # 75% data for analysis

# predict the data
y_pred=knn.predict(x_test) # 25% of data is used for testing
#print(y_pred)

# import the metrics class
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test,y_pred)
print(cnf_matrix)

# import required modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

class_names= [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)
print
# create headmap
sns.heatmap(pd.DataFrame(cnf_matrix),annot=True,cmap="Greens",fmt="d",annot_kws={"size":10})
ax.xaxis.set_label_position("bottom")
plt.tight_layout()
plt.title("confusion matrix", y=1.4)
plt.xlabel('actual label')
plt.xlabel('predicated labels')
precision = metrics.precision_score(y_test,y_pred,average="macro")

# plt.show

print("accuracy of the model:",metrics.accuracy_score(y_test,y_pred))
#print("precision of the model :",metrics.precision_score(y_test,y_pred),average="macro")
#print("recall of the model:",metrics.recall_score(y_test,y_pred))
#print("f1 score of the model:",metrics.f1_score(y_test,y_pred))