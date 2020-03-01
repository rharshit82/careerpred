import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
df=pd.read_excel("dataset_students.xlsx")
for i in range (0,204):
    if(df['Do you like Computer programming?'][i]=='Yes'):
        df['Do you like Computer programming?'][i]=1
    elif(df['Do you like Computer programming?'][i]=='No'):
        df['Do you like Computer programming?'][i]=0
for i in range (0,204):
    if(df['Do you have interest in robotics,building design or hardware?'][i]=='Yes'):
        df['Do you have interest in robotics,building design or hardware?'][i]=1
    elif(df['Do you have interest in robotics,building design or hardware?'][i]=='No'):
        df['Do you have interest in robotics,building design or hardware?'][i]=0
for i in range (0,204):
    if(df['What do you see yourself in next 10 years?'][i]=='Well Settled life with average pay'):
        df['What do you see yourself in next 10 years?'][i]=1
    elif(df['What do you see yourself in next 10 years?'][i]=='Hectic life with higher pay'):
        df['What do you see yourself in next 10 years?'][i]=0
for i in range (0,204):
    if(df['What is your stream?'][i]=='Science'):
        df['What is your stream?'][i]=1
    elif(df['What is your stream?'][i]=='Commerce'):
        df['What is your stream?'][i]=0
    elif(df['What is your stream?'][i]=='Arts'):
        df['What is your stream?'][i]=2
for i in range (0,204):
    if(df['Choose any one of the following'][i]=='Money'):
        df['Choose any one of the following'][i]=1
    elif(df['Choose any one of the following'][i]=='Fame'):
        df['Choose any one of the following'][i]=0
for i in range (0,204):
    if(df['Do you love studying Mathematics and Science ?'][i]=='Yes'):
        df['Do you love studying Mathematics and Science ?'][i]=1
    elif(df['Do you love studying Mathematics and Science ?'][i]=='No'):
        df['Do you love studying Mathematics and Science ?'][i]=0
k=df[['Average marks you got in Science in your High School (9th and 10th class)',
       'Average marks you got in Maths in your High School (9th and 10th class)',
       'Mark your logical skills out of 10?',
       'Mark your memorizing skill capacity out of 10?',
       'How likely do you  want to learn new technologies  came to market?',
       'Do you have interest in robotics,building design or hardware?',
       'Do you like Computer programming?',
       'Choose any one of the following',
       'What do you see yourself in next 10 years?',
       'Do you love studying Mathematics and Science ?']]
regressor=LogisticRegression()
t=list(df['What is your stream?'])
regressor.fit(k,t)
pickle.dump(regressor,open('model.pkl','wb'))
