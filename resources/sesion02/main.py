import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

from model import Model

df = pd.read_pickle('../data/manifesto_uncased.df')
df = df[['phrase', 'label']]

X_train, X_test, y_train, y_test = train_test_split(df.phrase.to_numpy(), df.label.to_numpy(), 
                                                    test_size=0.20, random_state=2023)

X_train = X_train[0:10000] 
X_test  = X_test[0:10000] 
y_train = y_train[0:10000] 
y_test  = y_test[0:10000] 

model = Model(vectorization_type='tfidf')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Resultados de evaluacion")
print("-"*10)
print("Accuracy: {:0.4f}".format(accuracy_score(y_test, y_pred)))
print("F1-Score Macro: {:0.4f}".format(f1_score(y_test, y_pred, average='macro')))
