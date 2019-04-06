#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 10:59:34 2018

@author: xk_wang
"""

import pandas as pd
import numpy as np

df = pd.read_excel("博物馆-地铁500米到10000米范围.xlsx",sheet_name = 4)
def calculate_accessibility(df):
    data_dict = df.groupby("INPUT_FID").DISTANCE.apply(list).to_dict()
    #############################################################################
    new_dict = {}
    xiaoqu_ID = []
    accessibility = []
    number_railway = []
    for key in data_dict.keys():
        number_railway.append(len(data_dict[key]))
        new_dict[key] = np.average(data_dict[key])
        xiaoqu_ID.append(key)
        
    for value in new_dict.values():   
        accessibility.append(value)
    
    #to_dataframe = {"INPUT_FID":xiaoqu_ID,"Accessibility":accessibility}
    to_dataframe = {"INPUT_FID":xiaoqu_ID,"Accessibility":accessibility,"Railway_numbers":number_railway}
    df_new = pd.DataFrame(to_dataframe)
    
    #############################################################################
    #name = df['名称'].tolist()
    name_dict = df.groupby("名称").INPUT_FID.apply(list).to_dict()
    temp_dict = {}
    name_ID = []
    name = []
    
    for key in name_dict.keys():
        temp_dict[key] = name_dict[key][0]
        name.append(key)
    for value in temp_dict.values():
        name_ID.append(value)
    
    id_match = {"INPUT_FID":name_ID,"NAME":name}
    df_id_match = pd.DataFrame(id_match)
    df_id_match = df_id_match.sort_values("INPUT_FID")
    
    df_merge = pd.merge(df_new,df_id_match,on = 'INPUT_FID')
    ## reorder columns' name 
    df_merge = df_merge[[ 'NAME','INPUT_FID', 'Railway_numbers','Accessibility']]
    df_merge = df_merge.sort_values("Accessibility")
    
    return df_merge    

def random_remove(df,ratio):
    num2remove = int(len(df.INPUT_FID)*ratio)
    index2move = np.random.randint(low = 0,high = len(df.INPUT_FID),size = num2remove).tolist()
    df_remove = df.drop(index2move)
    df_remove.index = range(len(df_remove.INPUT_FID))
    
    return df_remove


df_original = calculate_accessibility(df)
## remove 10% node(地铁)
df_random_remove = calculate_accessibility(random_remove(df,0.1))

df_merge = pd.merge(df_original,df_random_remove,on = ['NAME','INPUT_FID'])

df_merge['Accessibility_reduce_ratio'] = 0
df_merge['Accessibility_nuber_reduce_ratio'] = 0
for i in range(len(df_merge.INPUT_FID)):
    df_merge.iloc[i,6] = (df_merge['Accessibility_y'][i] - df_merge['Accessibility_x'][i])/df_merge['Accessibility_x'][i]
    df_merge.iloc[i,7] = (df_merge['Railway_numbers_x'][i] - df_merge['Railway_numbers_y'][i])/df_merge['Railway_numbers_x'][i]

df_merge = df_merge[['NAME', 'INPUT_FID','Railway_numbers_x','Railway_numbers_y', 'Accessibility_nuber_reduce_ratio','Accessibility_x','Accessibility_y','Accessibility_reduce_ratio']]
# write to excel    
df_merge.to_excel("可达性分析-博物馆-地铁500米到10000米范围-10KM-破坏10%.xlsx")

