#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 23:35:02 2018

@author: xk_wang
"""

from selenium import webdriver
import re
import sys
stdo = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = stdo


#location = driver.find_element_by_xpath("//*[@id='pointInput']")
#location = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div/ul/li[1]/div/p").text

#get lat and lon from website 
def find_location(name):
    driver.find_element_by_id("localvalue").clear()
    driver.find_element_by_id("localvalue").send_keys(name)
    driver.find_element_by_id("localsearch").click()
    driver.find_element_by_id("no_0").click()
    location = driver.find_element_by_xpath("//*[@id='pointInput']").get_attribute("data-clipboard-text")
    
    temp = str(location)
    index = [m.start() for m in re.finditer(',',temp)]
    lon = temp[0:index[0]]
    lat = temp[index[0]+1:]
    return lat,lon


url = "http://api.map.baidu.com/lbsapi/getpoint/index.html"
driver = webdriver.Firefox()
driver.get(url)


#name = u"从化市中心医院"
f = open("广州市医院信息.txt","r")
lines = f.readlines()
f.close()

#get all hospitals' name
names = []
for line in lines:
    index = [m.start() for m in re.finditer(',',line)]
    name = line[0:index[0]]
    names.append(name)

#get and write locations for every hospital
push=r'auto_get_location.txt'
for item in names:
    try: 
        item = item.decode("utf-8") #solve encoding problems,with a prefix - 'u'
        location = find_location(item)
        lat = location[0]
        lon = location[1]
        
        f = open(push,'a')
        f.write(str(item.encode('utf-8'))+','+str(lat)+','+str(lon)+'\n')
        f.close()
    except Exception,e: 
            print e 
            







