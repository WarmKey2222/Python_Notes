#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:10:25 2018

@author: xk_wang
"""

from selenium import webdriver
import re
#from string import punctuation

url = "https://baike.baidu.com/"
driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_id("query").clear()
driver.find_element_by_id("query").send_keys(u"华南农业大学")
driver.find_element_by_id("search").click()

res = driver.page_source

#link = driver.current_url
#x = re.search("学校占地亩",res)
#x.span()

def get_suqare_infos(name):
    driver.find_element_by_id("query").clear()
    driver.find_element_by_id("query").send_keys(name)
    driver.find_element_by_id("search").click()
    
    res = driver.page_source
    reg = re.compile(u"占地+\d{1,7}.*[平方米|亩]")
    x= re.findall(reg,res)
    
    return x

f = open("广州白云区大学.txt","r")
lines = f.readlines()
f.close()

names = []
for line in lines:
    index = [m.start() for m in re.finditer(',',line)]
    name = line[0:index[0]]
    names.append(name)

push=r'广州白云区大学_mianji.txt'
for item in names:
    try: 
        item = item.decode("utf-8") #solve encoding problems,with a prefix - 'u'
        location = get_suqare_infos(item)
        
        f = open(push,'a')
        f.write(str(item.encode('utf-8'))+','+str(location[0].encode('utf-8'))+'\n')
        f.close()
    except Exception,e: 
            print e 

"""
reg = re.compile(r'[\w].*\d$]+')
x = re.findall(reg,res)

reg = re.compile("专任教师+\d{1,7}")
x= re.findall(reg,res)

reg = re.compile("占地+\d?|学校占地+\d?|专任教师+\d?.*[平方米|亩]")
x= re.findall(reg,res)
"""



