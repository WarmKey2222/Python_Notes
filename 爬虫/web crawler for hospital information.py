#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:40:11 2018

@author: xk_wang
"""

from selenium import webdriver
from time import sleep
import time
import sys
stdo = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')
sys.stdout = stdo

def get_hospital_info(url):
    
    driver.get(url)
    hospital_name = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[1]/h1").text
    hospital_district = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td[4]/a").text
    hospital_build_year = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[4]/span").text
    hospital_type = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[6]/span").text
    hospital_level = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[2]/span").text
    hospital_department_number = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[4]/a").text
    hospital_medical_number = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[6]/a").text
    hospital_beds_number = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[2]/span").text
    hospital_years_menzhenliang = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[4]/span").text
    hospital_whether_yibao = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[6]/span").text
    hospital_address = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/dl/dd/p[4]/em").text
    return(hospital_name,hospital_district,hospital_build_year,hospital_type
           ,hospital_level,hospital_department_number,hospital_medical_number,hospital_beds_number
           ,hospital_years_menzhenliang,hospital_whether_yibao,hospital_address)


###############################################################################
url = "https://yyk.99.com.cn/guangzhou/"
driver = webdriver.Firefox()
links=[]

###############################################################################
driver.get(url)

qu_id = [2,3,4,5,6,7,8,9,10,11,13]
for id_number in qu_id:
    path = "/html/body/div[5]/div[1]/div[2]/div["+str(id)+"]/div/table/tbody/tr/td/a"
    items= driver.find_elements_by_xpath(path)
    for item in items: 
        links.append(item.get_attribute('href'))
        
"""        
#越秀区
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[2]/div/table/tbody/tr/td/a")
#荔湾区
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[3]/div/table/tbody/tr/td/a")
#海珠区
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[4]/div/table/tbody/tr/td/a")
#天河区(98)
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[5]/div/table/tbody/tr/td/a")
#白云区(117)
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[6]/div/table/tbody/tr/td/a")
#黄埔区(34)
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[7]/div/table/tbody/tr/td/a")
#番禺区(53)
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[8]/div/table/tbody/tr/td/a")
#花都区(25)
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[9]/div/table/tbody/tr/td/a")
#增城市(40)
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[10]/div/table/tbody/tr/td/a")
#从化市(27)
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[11]/div/table/tbody/tr/td/a")
#南沙区(11)
items= driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div[2]/div[13]/div/table/tbody/tr/td/a")
"""

#change div[5] to div[4]
#"/html/body/div[5]/div[1]/div[2]/div[2]/div/table/tbody/tr/td/a"
for item in items: 
    links.append(item.get_attribute('href'))

driver.quit() 
###############################################################################
#https://yyk.99.com.cn/yuexiu/69952/jianjie.html
import re
push=r'广州市医院.txt' 
for link in links:
    index = [m.start() for m in re.finditer('/',link)]
    hospital_id = link[index[3]+1:]
    url='https://yyk.99.com.cn/liwan/'+hospital_id+'jianjie.html'
    try: 
        temp = get_hospital_info(url)
        f=open(push,'a')
        f.write(str(temp[0])+','+str(temp[1])+','+str(temp[2])+','+str(temp[3])+','+str(temp[4])+','+str(temp[5])+
                ','+str(temp[6])+','+str(temp[7])+','+str(temp[8])+','+str(temp[9])+','+str(temp[10])+'\n')
        f.close()
    except Exception,e: 
            print e 

"""
#医院别名
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td[1]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td[2]/span
#所在地区
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td[3]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[1]/td[4]/a
#院长姓名
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[1]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[2]/span
#建院年份
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[3]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[4]/span
#医院类型
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[5]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[6]/span
#医院等级
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[1]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[2]/span
#科室数量
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[3]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[4]/a
#医护人数
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[5]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[6]/a
#病床数量
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[1]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[2]/span
#年门诊量
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[3]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[4]/span
#是否医保
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[5]/span
/html/body/div[6]/div[3]/div[1]/div[1]/table/tbody/tr[4]/td[6]/span
"""


"""
#越秀区(136) 
/html/body/div[5]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/a
/html/body/div[5]/div/div[2]/div[2]/div/table/tbody/tr[34]/td[4]/a

#荔湾区(72)
/html/body/div[5]/div/div[2]/div[3]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[3]/div/table/tbody/tr[18]/td[4]/a

#海珠区(75)
/html/body/div[5]/div/div[2]/div[4]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[4]/div/table/tbody/tr[19]/td[3]/a

#天河区(98)
/html/body/div[5]/div/div[2]/div[5]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[5]/div/table/tbody/tr[25]/td[2]/a

#白云区(117)
/html/body/div[5]/div/div[2]/div[6]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[6]/div/table/tbody/tr[30]/td/a

#黄埔区(34)
/html/body/div[5]/div/div[2]/div[7]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[7]/div/table/tbody/tr[9]/td[2]/a

#番禺区(53)
/html/body/div[5]/div/div[2]/div[8]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[8]/div/table/tbody/tr[14]/td/a

#花都区(25)
/html/body/div[5]/div/div[2]/div[9]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[9]/div/table/tbody/tr[7]/td/a

#增城市(40)
/html/body/div[5]/div/div[2]/div[10]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[10]/div/table/tbody/tr[10]/td[4]/a

#从化市(27)
/html/body/div[5]/div/div[2]/div[11]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[11]/div/table/tbody/tr[7]/td[3]/a

#南沙区(11)
/html/body/div[5]/div/div[2]/div[13]/div/table/tbody/tr[1]/td[1]/a
/html/body/div[5]/div/div[2]/div[13]/div/table/tbody/tr[3]/td[3]/a

"""






