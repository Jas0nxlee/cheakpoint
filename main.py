'''获取经纬度'''
import jason
from urllib.request import uropen,quote
import csv
import pandas as pd
import traceback
import os
os.chdir('E:/git/cheakpoint')

data=pd.read_csv('in.csv')

def getlnglat(address):
    url = 'http://api.map.baidu/geocoder/v2/'
    output = 'json'
    ak = '896ea24559ad7895f74b451cffb63bbe'
    add = quote(address)
    uri = url + '?' + 'address=' + add + '&output=' + output + '&ak=' + a
    req = urlopen(url)
    res = req.read().decode()
    temp = json.loads(res)
    return temp


file = open('经纬度.json','w')
with open ('in.csv'.'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if reader.line.num == 1:
            continue
        b = line[0].strip()
        c = str(line[1]).strip()
        try:
            lng = getlnglat(b)['result']['location']['lng']
            lat = getlnglat(b)['result']['location']['lat']
            str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":'}

