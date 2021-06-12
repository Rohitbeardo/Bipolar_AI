
import pandas as pd
import sklearn
import pickle

data=pd.read_csv("patient.csv")
data.head()



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(data.loc[:,data.columns != "episode"], 
                                                    data["episode"], test_size=0.2)

"""Decision tree"""

from sklearn import tree

dt =tree.DecisionTreeClassifier(max_depth=10, min_samples_leaf=15)
dt.fit(X_train, y_train)

print(dt.score(X_test,y_test))

pickle.dump(log_reg,open('input.pkl','wb'))
model=pickle.load(open('input.pkl','rb'))