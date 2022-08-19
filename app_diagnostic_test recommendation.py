#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 07:50:31 2022

@author: faithtoo
"""

#Import main library
import numpy as np

#Import Flask modules
from flask import Flask, request

#Import pickle to save our recommendation model
import pickle 


app = Flask(__name__)

#Open our model 
model = pickle.load(open('diagnostic_test_recommendation.pkl','rb'))



#Set a post method to yield predictions on page
@app.route('/', methods = ['POST'])
def predict():
    
    #obtain all form values and place them in an array, convert into integers
    int_features = [int(x) for x in request.form.values()]
    #Combine them all into a final numpy array
    final_features = [np.array(int_features)]
    #predict the price given the values inputted by user
    prediction = model.predict(final_features)
    
    
    output = prediction[0]
    
   
#Run app
if __name__ == "__main__":
    app.run(debug=True)