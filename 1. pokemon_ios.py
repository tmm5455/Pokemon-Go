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
for dirs in os.listdir('./data/'):
    for files in os.listdir('./data/{}'.format(dirs)):
        if 'ios' in files:
            urls.append(str('file:///C:/Users/Tanvi%20Mehta/Downloads/data/{}/{}'.format(dirs,files)))
f = open('pokemon_ios.json','w')
f.write('[')
for date in daterange(start, end):
    for url in urls:
        if str(date) in url:
            r = urllib.request.urlopen(url).read()
            soup = BeautifulSoup(r,'lxml')
            print('Collecting for file {}'.format(url))
            #finds no. of ratings in current version
            rating = soup.find('div','extra-list customer-ratings')
            
            dic_attr["total_rating_current_version"] = int(rating.find_all('div')[1].get_text()[-14:-8].strip())
            try:
                #finds no. of ratings in all versions
                dic_attr["total_rating"] = int(rating.find_all('div')[4].get_text()[:-8].strip())
                
            except:
                dic_attr["total_rating"] = int(rating.find_all('div')[1].get_text()[:-8].strip())
            #finds file size in MB
            size_ver = soup.find('ul','list')
            dic_attr["file_size"] = int(size_ver.find_all('li')[-4].get_text()[-6:-2].strip())
                                    
            #finds description text
            dic_attr["description"] = soup.find('div','platform-content-block display-block').find_all('p')[1].get_text()

            #finds version
            dic_attr['version'] = str(size_ver.find_all('span')[-6])[-12:-7].strip()
            
            dic["{}_{}_{}_{}".format(date.year,date.strftime('%m'),date.strftime('%d'),url[-22:-17])] = dic_attr
           
    json.dump(dic,f,sort_keys=True,indent=4)
    if date.month == 10 and date.day == 31 and url[-22:-17] == "23_50":
        break
    f.write(',')
    dic={}
f.write(']')
f.close()
    
#print(sizes)
#print('\n\n{}'.format(all_ratings))
#print('\n\n{}'.format(cur_ratings))
 



                     