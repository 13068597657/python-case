# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:32:10 2020

@author: egnxxfx
"""

import  pandas as pd
import os
import re

print(os.getcwd())

PP_PriceItem_Output=pd.DataFrame(columns=['Site','Article No','Description'])

path=os.getcwd()
pack=[]
for root,dirs,files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == '.xlsx':
            #Pack.append(file)
            file_name = os.path.join(root, file)
            print(file_name)
            pack_nro = list(pd.read_excel(file_name, nrows=1,sheet_name='detail')) 
            suo_yin_1 = df_1.index("Site")
            suo_yin_2 = df_1.index("Our Order No.")
            df = pd.read_excel(file_name, usecols=[suo_yin_1, suo_yin_2],sheet_name='detail') 
            df.drop([len(df)-1],inplace=True)
            #print(df)
            excel_name = file.replace(".xlsx", "")      # 提取每个excel文件的名称，去掉.xlsx后缀
            print(excel_name)
            df["批次"] = excel_name       # 新建列名为“店铺”，列数据为excel文件名
            pack.append(df)  
pack_lsit = pd.concat(pack)

pack_lsit.to_excel('./total/pack list.xls',sheet_name='汇总')


    