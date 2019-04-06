#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:10:11 2018

@author: xk_wang
"""

import pandas as pd
import re

df_xiaoqu_original = pd.read_excel("广州小区汇总.xlsx",sheet_name = 0)

df_xiaoqu = pd.read_excel("可达性分析-小区-地铁500米到10000米范围-1KM-破坏10%.xlsx",sheet_name = 0)
df_match = df_xiaoqu_original[['小区名称','平均房价','建造年份','绿化率']]
df_match.columns = ['NAME', '平均房价', '建造年份', '绿化率']

df_merge = pd.merge(df_xiaoqu,df_match,on = ['NAME'])

df_merge_affected = df_merge.ix[df_merge['Accessibility_nuber_reduce_ratio']>0,:]

affected_house_price = df_merge.ix[df_merge['Accessibility_nuber_reduce_ratio']>0 ,'平均房价'].tolist()
#retirve number from string
for item in range(len(affected_house_price)):
    if affected_house_price[item] != '暂无数据':
        index = [m.start() for m in re.finditer('元',affected_house_price[item])]
        affected_house_price[item] = affected_house_price[item][0:index[0]]
df_merge_affected['平均房价'] = affected_house_price

#affected_Accessibility_x = df_merge.ix[df_merge['Accessibility_nuber_reduce_ratio']>0 ,'Accessibility_x'].tolist()
affected_house_build_year = df_merge.ix[df_merge['Accessibility_nuber_reduce_ratio']>0 ,'建造年份'].tolist()
for item in range(len(affected_house_build_year)):
    if affected_house_build_year[item] != '暂无数据':
        index = [m.start() for m in re.finditer('年',affected_house_build_year[item])]
        affected_house_build_year[item] = affected_house_build_year[item][0:index[0]]
df_merge_affected['建造年份'] = affected_house_build_year

affected_house_green_ratio = df_merge.ix[df_merge['Accessibility_nuber_reduce_ratio']>0 ,'绿化率'].tolist()
for item in range(len(affected_house_green_ratio)):
    if affected_house_green_ratio[item] != '暂无数据':
        index = [m.start() for m in re.finditer('%',affected_house_green_ratio[item])]
        affected_house_green_ratio[item] = affected_house_green_ratio[item][0:index[0]]
for item in range(len(affected_house_green_ratio)):
    if affected_house_green_ratio[item] != '暂无数据':
        affected_house_green_ratio[item] = float(affected_house_green_ratio[item])/100
df_merge_affected['绿化率'] = affected_house_green_ratio

df_merge_affected_with_full_house_price = df_merge_affected.ix[df_merge_affected['平均房价']!='暂无数据',:]
df_merge_affected_with_full_build_year = df_merge_affected.ix[df_merge_affected['建造年份']!='暂无数据',:]
df_merge_affected_with_full_green_ratio = df_merge_affected.ix[df_merge_affected['绿化率']!='暂无数据',:]

df_merge_affected_with_full_house_price.to_excel("all-data-可达性分析-小区-地铁500米到10000米范围-1KM-破坏10%.xlsx")


df_final_analysis = pd.merge(df_merge_affected_with_full_house_price,df_merge_affected_with_full_build_year,on = ['NAME', 'INPUT_FID', 'Railway_numbers_x', 'Railway_numbers_y',
       'Accessibility_nuber_reduce_ratio', 'Accessibility_x','Accessibility_y', 'Accessibility_reduce_ratio','绿化率'])
df_final = df_final_analysis[['NAME','Railway_numbers_x', 'Railway_numbers_y',
       'Accessibility_nuber_reduce_ratio', 'Accessibility_x',
       'Accessibility_y', 'Accessibility_reduce_ratio','平均房价_x', '建造年份_x']]
df_final.columns = ['NAME','Railway_numbers_x', 'Railway_numbers_y',
       'Accessibility_nuber_reduce_ratio', 'Accessibility_x',
       'Accessibility_y', 'Accessibility_reduce_ratio','aver_house_price', 'build_year']
df_final[['Railway_numbers_x', 'Railway_numbers_y',
       'Accessibility_nuber_reduce_ratio', 'Accessibility_x',
       'Accessibility_y', 'Accessibility_reduce_ratio','aver_house_price', 'build_year']]=df_final[['Railway_numbers_x', 'Railway_numbers_y',
       'Accessibility_nuber_reduce_ratio', 'Accessibility_x',
       'Accessibility_y', 'Accessibility_reduce_ratio','aver_house_price', 'build_year']].apply(pd.to_numeric)

df_final = df_final.sort_values("aver_house_price",ascending=False)
#corr = df_final.corr()

import seaborn as sns
import matplotlib.pyplot as plt
def test(df):
    dfData = df.corr()
    plt.subplots(figsize=(8, 8)) # 设置画面大小
    sns.heatmap(dfData, annot=True, vmax=1, square=True, cmap="Blues")
    plt.savefig('./correlation.png')
    plt.show()

#ananylis top 100 sorted by house_price
test(df_final.iloc[0:200,:])
test(df_final)





