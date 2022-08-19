#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:33:34 2022

@author: faithtoo
"""


import requests

# change the url and r values 

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'score':5 })

print(r.json())