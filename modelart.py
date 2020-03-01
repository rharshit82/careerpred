import pandas as pd
import numpy as numpy
import pickle
from sklearn.linear_model import LogisticRegression
df=pd.read_csv("artdata.csv")
x=df[['Rate your communication skill:', 'Rate your creativity skill:',
       'Rate your Decision thinking Skills', 'Rate your drawing ability:',
       'Rate your investigative skills:']]
y=df[[' Profession']]
modelart=LogisticRegression()
modelart.fit(x,y)
pickle.dump(modelart,open('modelart.pkl','wb'))
