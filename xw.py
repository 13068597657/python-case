# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 13:34:14 2020

@author: egnxxfx
"""

import  pandas as pd
import os
import re

#print(os.getcwd())

####读取当前目录的xlsx文件类型####
# =============================================================================
# All_doc_indir =os.listdir()
# 
# for i in All_doc_indir:
#     match = re.search('.*xls.*',i)
#     if match:
#         print(i)
# =============================================================================
       

####读取固定名称EXECL表格####
# =============================================================================
# dir='C:/Users/EGNXXFX/Desktop/Exercise/Exercise V1/源数据表格.xlsx'
# df = pd.read_excel(dir,sheet_name='主设备')
# #print(df)
# ####读取特定条件列，并汇总求和####
# df_sum=df.groupby(['型号','物料编码','物料名称'])['数量',].sum()
# #print(df_sum)
# ####修改新要求的列名####
# df_sum.columns=['汇总']
# ####输出到一份新的EXECL####
# 
# df_sum.to_excel('./pivotable list.xlsx',sheet_name='pivotable')
# #print(df_sum)
# =============================================================================


