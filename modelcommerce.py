import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
df=pd.read_csv("commercedata.csv")
x=df[['Rate your interest in mathematics:',
       'Rate your interest in knowing about stock market:',
       'Rate your ability to influence others:',
       'Rate your leadership quality:', 'Rate your communication skills:']]
y=df[[' Profession']]
modelcommerce=LogisticRegression()
modelcommerce.fit(x,y)
pickle.dump(modelcommerce,open('modelcommerce.pkl','wb'))
