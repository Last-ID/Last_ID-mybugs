#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import csv
import json
import pandas as pd
#---------用pandas库，filename写你自己的--------------
filename="data.json"
with open(filename,'r',encoding='utf-8') as f:
  trump_list=json.load(f)
frame=pd.DataFrame(trump_list)
print(frame)
frame.to_csv("trump_meet.csv")
