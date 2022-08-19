#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:46:07 2022

@author: faithtoo
"""
# to be used for student categorization  and diagnostin test recommendation
import requests

# change the url and r values 
url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'score':2})

print(r.json())