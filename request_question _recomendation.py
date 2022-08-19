#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:00:44 2022

@author: faithtoo
"""

import requests

# change the url and r values 

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'question_level_code':5,'marked':0 })

print(r.json())