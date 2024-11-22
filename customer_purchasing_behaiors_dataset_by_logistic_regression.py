# -*- coding: utf-8 -*-
"""customer purchasing behaiors dataset by logistic regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lmid-KjFtmHXOqasFgxab3zzYGTrzexG
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
df = pd.read_csv("/content/Customer Purchasing Behaviors.csv")
#print(df.head)
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
#df['Gender']=le.fit_transform(df['Gender'])
#print(df.head)
x = df[[ 'Gender','Age','EstimatedSalary']]
y = df["Purchased"]
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
print(y_pred)

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
# plt.show

print("accuracy of the model:",metrics.accuracy_score(y_test,y_pred))
print("precision of the model:",metrics.precision_score(y_test,y_pred))