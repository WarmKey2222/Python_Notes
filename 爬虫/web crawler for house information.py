#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 22:31:58 2018

@author: xk_wang
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from collections import Counter
from time import sleep
import MySQLdb
import requests
import time
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#定义函数：获取小区数据
def get_xiaoqu_info(link):
    xiaoqu_id=link[34:len(link)-1]
    #url='https://dg.anjuke.com/community/view/'+xiaoqu_id
    url='https://gz.anjuke.com/community/view/'+xiaoqu_id
    driver.get(url)
    tmp= driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/h1").text
    xiaoqu_name=tmp[0:tmp.find(' ')] #小区名称 
    xiaoqu_zq=tmp[tmp.find(' ')+1:tmp.find('-')] #小区所属镇区 
    xiaoqu_addr=tmp[tmp.find(' ')+1:] #小区地址
    tmp= driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/a").get_attribute('href') 
    lat=tmp[tmp.find('l1=')+3:tmp.find('&')] #维度 
    lng=tmp[tmp.find('l2=')+3:tmp.find('l3')-1] #经度
    price_avg= driver.find_element_by_xpath("//*[@id='basic-infos-box']/div[1]/span[1]").text 
    tmp= driver.find_element_by_xpath("//*[@id='commhousedesc']/span[2]").text 
    price_class=tmp[0:2] #价格比类型 
    month=tmp[tmp.find('环比')+2:tmp.find('月')] #上个月月份
    # 上升为1，下降为-1
    if '↑' in tmp :
         price_type=1 
         price_rate= tmp[tmp.find('↑')+1:] #变化率 
    else :
         price_type=-1 
         price_rate= tmp[tmp.find('↓')+1:] #变化率
         
    #物业信息
    #物业类型
    property_type=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[1]").text
    #物业费 
    property_price=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[2]").text 
    #总建筑面积 
    total_building_area=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[3]").text 
    #总户数 
    total_house_count=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[4]").text 
    #建造年代 
    building_time=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[5]").text 
    #停车位 
    parking_count=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[6]").text 
    #容积率 
    floor_area_ratio=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[7]").text 
    #绿化率 
    greening_rate=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[8]").text 
    #开发商 
    developer=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[9]").text 
    #物业公司 
    property_company=driver.find_element_by_xpath("//*[@id='basic-infos-box']/dl/dd[10]").text 
    #占地面积
    try : 
        tmp=driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[1]/div[1]/div[2]/p").text 
        if (u'占地面积' in tmp) & (u'平方米' in tmp) : 
            floor_aera = tmp[tmp.find('占地')+4:tmp.find('平方米')+3] 
        elif (u'占地' in tmp) & (u'平方米' in tmp): 
            floor_aera = tmp[tmp.find('占地')+2:tmp.find('平方米')+3] 
        elif (u'占地面积' in tmp) & (u'亩' in tmp): 
            floor_aera = tmp[tmp.find('占地')+4:tmp.find('亩')+1] 
        elif (u'占地' in tmp) & (u'亩' in tmp): 
            floor_aera = tmp[tmp.find('占地')+2:tmp.find('亩')+1] 
        else : 
            floor_aera=u"暂无数据" 
    except (ZeroDivisionError,Exception) as e: 
        floor_aera =u"暂无数据" 
        print e 
        pass 

    #创建时间 
    created_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    #二手房源数 
    second_house=driver.find_element_by_xpath("//*[@id='basic-infos-box']/div[2]/a[1]").text 
    #租房源数 
    rental_house=driver.find_element_by_xpath("//*[@id='basic-infos-box']/div[2]/a[2]").text 
    return (xiaoqu_id,xiaoqu_name,xiaoqu_zq,xiaoqu_addr,lat,lng,price_avg,price_class,month,price_type,price_rate 
            ,property_type,property_price,total_building_area,total_house_count,building_time,parking_count 
            ,floor_area_ratio,greening_rate,developer,property_company,floor_aera,second_house,rental_house,created_date) 

#定义函数：链接导入数据库 
def to_sql(data): 
    #根据自己的数据设置参数 
    conn=MySQLdb.connect("localhost","root","pwd","test",charset="utf8" ) 
    cursor = conn.cursor() 
    sql_create_database = 'create database if not exists test' 
    cursor.execute(sql_create_database)

    cursor.execute('''create table if not exists test.xiaoqu(xiaoqu_id bigint(80),
                                                              xiaoqu_name varchar(50),
                                                              xiaoqu_zq varchar(50),
                                                              xiaoqu_addr varchar(50),
                                                              lat varchar(20),
                                                              lng varchar(20),
                                                              price_avg varchar(20),
                                                              price_class varchar(10),
                                                              month tinyint,
                                                              price_type tinyint,
                                                              price_rate varchar(10),
                                                              property_type varchar(20),
                                                              property_price varchar(10),
                                                              total_building_area varchar(20),
                                                              total_house_count varchar(10),
                                                              building_time varchar(10),
                                                              parking_count varchar(10),
                                                              floor_area_ratio varchar(10),
                                                              greening_rate varchar(10),
                                                              developer varchar(50),
                                                              property_company varchar(50),
                                                              floor_aera varchar(20),
                                                              second_house varchar(10),
                                                              rental_house varchar(10),
                                                              created_date DATETIME,
                                                              primary key (xiaoqu_id,month));''') 
    cursor.executemany('insert ignore into test.xiaoqu values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',data) 
    cursor.execute('select * from test.xiqoqu limit 5;')

    conn.commit()
    cursor.close()
    conn.close()
    
#url = "https://m.anjuke.com/dg/xiaoqu-p"
url = "https://m.anjuke.com/gz/xiaoqu-p"
driver = webdriver.Firefox()
#driver.quit()
links=[]
for item in range(1,6): 
    urls=url+str(item) 
    #driver = webdriver.Firefox() 
    driver.get(urls) 
    zq_items= driver.find_elements_by_xpath("//*[@id='mapBody']/section/div/section/div[2]/div/a") 
    for zq_item in zq_items: 
        links.append(zq_item.get_attribute('href')) 
        sleep(0.01) 


infos = [] 
rate = 1 
for link in links : 
    if rate % 300 ==0 : 
        driver.quit() 
        driver = webdriver.Firefox() 
    try: 
        print "Getting information of the",rate,"-th xiqoqu." 
        infos.append(get_xiaoqu_info(link)) 
        #sleep(0.5) 
    except Exception,e: 
            print e 
            
    rate+=1 
    
print to_sql(infos)

    
    