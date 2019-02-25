'''获取经纬度'''
import json
from urllib.request import urlopen,quote
import csv
import pandas as pd
import traceback
import os
os.chdir('E:/git/cheakpoint')

data=pd.read_csv('in.csv')

def getlnglat(address):
    url = 'http://api.map.baidu.com/geocoder'
    output = 'json'
    ak = '896ea24559ad7895f74b451cffb63bbe'
    add = quote(address)
    uri = url + '?key=' + ak + '&output=json&address=' + add
    print(uri)
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    return temp


file = open('经纬度.json','w')
with open ('in.csv','r',encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        if reader.line_num == 1:
            continue
        b = line[0].strip()
        c = str(line[1]).strip()
        try:
            lng = getlnglat(b)['result']['location']['lng']
            lat = getlnglat(b)['result']['location']['lat']
            str_temp = '{"lat":' + str(lat) + ',"lng":' + str(lng) + ',"count":' + str(c) +'},'
            file.write(str_temp)
        except:
            f=open("异常日志.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            print('发生异常')
file.close()
