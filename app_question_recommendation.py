#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 07:52:20 2022

@author: faithtoo
"""

#Import main library
import numpy as np

#Import Flask modules
from flask import Flask, request

#Import pickle to save our regression model
import pickle 

#Initialize Flask and set the template folder to "template"
app = Flask(__name__)

#Open our model 
model = pickle.load(open('question_recommendation.pkl','rb'))


    
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

   
#Run app
if __name__ == "__main__":
    app.run(debug=True)