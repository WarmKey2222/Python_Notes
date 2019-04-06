#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 08:06:20 2018

@author: xk_wang
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df_xiaoqu_data = pd.read_excel("all-data-可达性分析-小区-地铁500米到10000米范围-2KM-破坏10%.xlsx",sheet_name = 0)

#x = df_xiaoqu_data['Railway_numbers_x']
#y = df_xiaoqu_data['平均房价']

sns.boxplot(df_xiaoqu_data.平均房价,orient='v')


data_dict = df_xiaoqu_data.groupby("Railway_numbers_x").平均房价.apply(list).to_dict()

data_dict_distance = df_xiaoqu_data.groupby("Accessibility_x").平均房价.apply(list).to_dict()
#############################################################################
def convert_data(data_dict):
    new_dict = {}
    xiaoqu_ID = []
    accessibility = []
    for key in data_dict.keys():
        new_dict[key] = np.average(data_dict[key])
        xiaoqu_ID.append(key)
        
    for value in new_dict.values():   
        accessibility.append(value)
    
    to_dataframe = {"Accessibility":xiaoqu_ID,"平均房价":accessibility}
    
    df_new = pd.DataFrame(to_dataframe)
    return df_new



df_xiaoqu_data.iloc[0:10,:].plot('Railway_numbers_x','平均房价',kind='scatter',subplots = True)
df_xiaoqu_data.iloc[0:10,:].plot('Accessibility_x','平均房价',kind='scatter',subplots = True)


data_number_Accessibility = convert_data(data_dict)
data_number_Accessibility.plot('Accessibility','平均房价',kind = 'scatter')

data_distance_Accessibility = convert_data(data_dict_distance)
data_distance_Accessibility.plot('Accessibility','平均房价',kind = 'scatter')

temp = df_xiaoqu_data.iloc[0:2000,:]
plt.subplot(121)
plt.scatter(temp.Railway_numbers_x,temp.平均房价)
plt.xlabel('Number_Accessibility')
plt.ylabel('House_Price')
plt.subplot(122)
plt.scatter(temp.Accessibility_x,temp.平均房价)
plt.xlabel('Distance_Accessibility')

plt.savefig('./Accessibility-top-2000.png')
###############################################################################

plt.subplot(121)
plt.scatter(data_number_Accessibility.Accessibility,data_number_Accessibility.平均房价)
plt.xlabel('Number_Accessibility')
plt.ylabel('Average_House_Price')
plt.subplot(122)
plt.plot(data_number_Accessibility.Accessibility,data_number_Accessibility.平均房价)
plt.xlabel('Number_Accessibility')

plt.savefig('./范围-2KM-破坏10%-Number_Accessibility-Average_House_Price.png')

