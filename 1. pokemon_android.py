# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import urllib
import os
import datetime
import json
import re
start = datetime.date(year=2016,month=7,day=21)
end = datetime.date(year=2016,month=10,day=31)
urls,num=[],[]
cur_ratings,all_ratings,sizes=[],[],[]
dic,dic_attr={},{}
def daterange(start_date,end_date):
    if start_date != end_date:
        for n in range((end_date - start_date).days + 1 ):
            yield start_date + datetime.timedelta(n)
    else:
        for n in range((start_date - end_date).days + 1):
            yield start_date - datetime.timedelta(n)
def conv_to_int(text):
    return int(re.sub(r"[\s,.]", "", text))
            
for dirs in os.listdir('./data/'):
    for files in os.listdir('./data/{}'.format(dirs)):
        if 'android' in files:
            urls.append(str('file:///C:/Users/Tanvi%20Mehta/Downloads/data/{}/{}'.format(dirs,files)))
f = open('pokemon_android.json','w')
f.write('[')
for date in daterange(start, end):
    for url in urls:
        if str(date) in url:
            r = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(r,'lxml')
            print('Collecting for file {}'.format(url))
            dic_attr['average_rating'] = float(str(soup.find('div','stars-container'))[53:58].strip())
            
            #finds no. of ratings in current version
            dic_attr['total_rating'] = conv_to_int(soup.find('div','stars-count').get_text().strip()[1:-1])

            try:
                dic_attr['rating_1'] = conv_to_int(soup.find_all('span','bar-number')[4].get_text())
                dic_attr['rating_2'] = conv_to_int(soup.find_all('span','bar-number')[3].get_text())
                dic_attr['rating_3'] = conv_to_int(soup.find_all('span','bar-number')[2].get_text())
                dic_attr['rating_4'] = conv_to_int(soup.find_all('span','bar-number')[1].get_text())
                dic_attr['rating_5'] = conv_to_int(soup.find_all('span','bar-number')[0].get_text())
            except:
                with open('log_pokemon_android.txt','a') as err:
                    err.write('Missing ratings in:{}/{}'.format(str(date),url[-26:-21]))
            #finds file size in MB
            try:
                dic_attr['file_size'] = int(soup.find_all('div','content')[1].get_text().strip()[0:-1])
            except:
                with open('log_pokemon_android.txt','a') as err:
                    err.write('Missing file_size in:{}/{}'.format(str(date),url[-26:-21]))
            #finds current version
            try:
                dic_attr['version'] = soup.find_all('div','content')[3].get_text().strip()
            except:
                dic_attr['version'] = soup.find_all('div','content')[2].get_text().strip()
            #finds description text
            dic_attr['description'] = soup.find('div','show-more-content text-body').get_text()

            
            dic["{}_{}_{}_{}".format(date.year,date.strftime('%m'),date.strftime('%d'),url[-26:-21])] = dic_attr
    json.dump(dic,f,sort_keys=True,indent=4)
    if date.month == 10 and date.day == 31 and url[-26:-21] == "23_50":
        break
    f.write(',')
    dic={}
f.write(']')
f.close()

 



                     