# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import division
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
# the histogram of the data
infile = open('pokemon_android.json').read()
lst_of_dicts = json.loads(infile)
v1,v2,v3,vr1,vr2,vr3,vr4,vr5=[],[],[],[],[],[],[],[]
tot_rating,avg_rating,size,r1,r2,r3,r4,r5=[],[],[],[],[],[],[],[]
d1={}
for dic in lst_of_dicts:
    for key in dic.keys():
            d = dic[key]
            v1.append(d["total_rating"])
            v2.append(d["average_rating"])
            v3.append(d["file_size"])
            vr1.append(d["rating_1"])
            vr2.append(d["rating_2"])
            vr3.append(d["rating_3"])
            vr4.append(d["rating_4"])
            vr5.append(d["rating_5"])
    tot_rating.append(np.mean(v1))
    avg_rating.append(np.mean(v2))
    size.append(np.mean(v3))
    r1.append(np.mean(vr1))
    r2.append(np.mean(vr2))
    r3.append(np.mean(vr3))
    r4.append(np.mean(vr4))
    r5.append(np.mean(vr5))
    v1,v2,v3,vr1,vr2,vr3,vr4,vr5=[],[],[],[],[],[],[],[]
i = 0   
for date in daterange(start,end):
    d1[str(date)] = list([tot_rating[i],avg_rating[i],size[i],r1[i],r2[i],r3[i],r4[i],r5[i]])
    i+=1

df = pd.DataFrame.from_dict(d1,orient='index')
df.columns=['total_rating',
            'avg_rating',
            'file_size',
            'rating_1',
            'rating_2',
            'rating_3',
            'rating_4',
            'rating_5']
pd.to_datetime(df.index)
df = df.sort_index()
    
fig, (axis1,axis2,axis3,axis4,axis5,axis6,axis7,axis8) = plt.subplots(8,1,squeeze=True,sharex=True,figsize=(20,30))

ax1 = sns.barplot(x=df.index, y='total_rating', data=df, ax=axis1)
ax2 = sns.barplot(x=df.index, y='avg_rating', data=df, ax=axis2)
ax3 = sns.barplot(x=df.index, y='file_size', data=df, ax=axis3)
ax4 = sns.barplot(x=df.index, y='rating_1', data=df, ax=axis4)
ax5 = sns.barplot(x=df.index, y='rating_2', data=df, ax=axis5)
ax6 = sns.barplot(x=df.index, y='rating_3', data=df, ax=axis6)
ax7 = sns.barplot(x=df.index, y='rating_4', data=df, ax=axis7)
ax8 = sns.barplot(x=df.index, y='rating_5', data=df, ax=axis8)
ax8.set_xticklabels(df.index.tolist(), rotation=90)
ax1.set_ylabel('Total Ratings')
ax2.set_ylabel('Average Ratings')
ax3.set_ylabel('File sizes')
ax4.set_ylabel('rating_1')
ax5.set_ylabel('rating_2')
ax6.set_ylabel('rating_3')
ax7.set_ylabel('rating_4')
ax8.set_ylabel('rating_5')