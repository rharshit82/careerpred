import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
df=pd.read_csv("pcm3.csv")
x=df[['Rate your understanding skills(how deeply you understand anything):',
       'Rate your interest for research:',
       'Rate your ability to explain things to others:',
       'Rate your interest in innovation:',
       'Rate your interest in performing experiments:',
       'how good you are in  complex problem solving :']]
y=df[[' Profession']]
modelpcm=LogisticRegression()
modelpcm.fit(x,y)
pickle.dump(modelpcm,open('modelpcm.pkl','wb'))
