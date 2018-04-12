# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 00:13:33 2016

@author: Tanvi Mehta
"""
import matplotlib.pyplot as plt
import seaborn as sns
import json
import datetime
import pandas as pd
import numpy as np

start = datetime.date(year=2016,month=7,day=21)
end = datetime.date(year=2016,month=10,day=31)

def daterange(start_date,end_date):
    if start_date != end_date:
        for n in range((end_date - start_date).days + 1 ):
            yield start_date + datetime.timedelta(n)
    else:
        for n in range((start_date - end_date).days + 1):
            yield start_date - datetime.timedelta(n)

infile = open('pokemon_ios.json').read()
lst_of_dicts = json.loads(infile)
v1,v2,v3=[],[],[]
tot_rating,cur_version,size=[],[],[]
d1={}
for dic in lst_of_dicts:
    for key in dic.keys():
            d = dic[key]
            v1.append(d["total_rating"])
            v2.append(d["total_rating_current_version"])
            v3.append(d["file_size"])
    tot_rating.append(np.mean(v1))
    cur_version.append(np.mean(v2))
    size.append(np.mean(v3))
    v1,v2,v3 = [],[],[]
i = 0   
for date in daterange(start,end):
    d1[str(date)] = list([tot_rating[i],cur_version[i],size[i]])
    i+=1

df = pd.DataFrame.from_dict(d1,orient='index')
df.columns=['total_rating','version_rating','file_size']
pd.to_datetime(df.index)
df = df.sort_index()

fig, (axis1,axis2,axis3) = plt.subplots(3,1,squeeze=True,sharex=True,figsize=(20,10))

ax1 = sns.barplot(x=df.index, y='total_rating', data=df, ax=axis1)
ax2 = sns.barplot(x=df.index, y='version_rating', data=df, ax=axis2)
ax3 = sns.barplot(x=df.index, y='file_size', data=df, ax=axis3)
ax1.set_ylabel('Total Ratings')
ax2.set_ylabel('Current Version Ratings')
ax3.set_xticklabels(df.index.tolist(), rotation=90)
ax3.set_ylabel('File sizes')
