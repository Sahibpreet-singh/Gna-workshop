import pandas as pd
from fastapi import FastAPI

import numpy as np 
import joblib 
import uvicorn
from Inputfile import StudentInput

app=FastAPI()
classifier=joblib.load("decision_tree.pkl")

@app.get('/')
def index():
    return {'message':'h'} 

@app.get('/{naam}')
def naamapi(naam:str):
    return {'welocme to':f'{naam}'}    

@app.post('/predict')
def prediction(data:StudentInput):
    data=data.model_dump()
    gender = data['gender']
    race_ethnicity = data['race/ethnicity']
    parental_level_of_education = data['parental level of education']
    lunch = data['lunch']
    test_preparation_course = data['test preparation course']
    math_score = data['math score']
    reading_score = data['reading score']
    writing_score = data['writing score']

    

if __name__=="__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)  