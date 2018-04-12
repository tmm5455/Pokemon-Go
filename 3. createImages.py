# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 16:18:40 2016

@author: Tanvi Mehta
"""

from bs4 import BeautifulSoup
import urllib
import os

urls=[]
images = []

for dirs in os.listdir('../data/'):
    for files in os.listdir('../data/{}'.format(dirs)):
        urls.append(str('file:///C:/Users/Tanvi%20Mehta/Downloads/data/{}/{}'.format(dirs,files)))
url='file:///C:/Users/Tanvi%20Mehta/Downloads/data/2016-07-21/00_20_pokemon_android.html'
#for url in urls:
#    print('Collecting from {}'.format(url))
r = urllib.request.urlopen(url).read()
soup = BeautifulSoup(r,'lxml')
#for image in 
image = soup.findAll("img")[-1]
x = ("%(src)s" % image)
print(x)
#        if x.endswith('jpeg') == True:
#            if x not in images:
#                images.append(x)
#out_folder = './output/'
#x = 0
#for file in images:
#    i = file
#    file = file.split('/')[-1]
#    x+=1
#    filename = str(x) + '.' + file
#    outpath = os.path.join(out_folder, filename)
#    urllib.request.urlretrieve(i,outpath)
