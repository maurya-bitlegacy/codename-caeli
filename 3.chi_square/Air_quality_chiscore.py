# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import csv
import json
import statistics 
from scipy.stats import chi2
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# %%
with open('../datasets/Final_Air_Quality_Data.csv', newline='') as f:
    reader = csv.reader(f)
    air_quality_list = list(reader)
# air_quality_list


# %%
air_quality_list=air_quality_list[1:]


# %%
air_quality={}
i=1
for ele in air_quality_list:
    air_quality[ele[0]]=air_quality.get(ele[0],{})
    l=[float(i) for i in ele[2:]]
    air_quality[ele[0]][ele[1]]=l
# air_quality


# %%
expected_values={}
for (k1,v1) in air_quality.items():
    for(k2,v2) in v1.items():
        expected_values[k2]=expected_values.get(k2,[0,0,0])
        #print(expected_values[k2])
        expected_values[k2][0]+=v2[0]
        expected_values[k2][1]+=v2[1]
        if(v2[2]<0):
            expected_values[k2][2]+=0
        else:
            expected_values[k2][2]+=v2[2]
        #print(expected_values[k2])
# expected_values


# %%
for (k,v) in expected_values.items():
    expected_values[k][:] = [(x/33) for x in expected_values[k]]
# expected_values


# %%
for (k,v) in expected_values.items():
    for i in range (0,3):
        expected_values[k][i]=round(expected_values[k][i],3)
# expected_values


# %%
air_data=[]
for (k1,v1) in air_quality.items():
    for (k2,v2) in v1.items():
        chi_statistics= 0
        mpc=0
        for i in range(0,3):
            chi_statistics+= ((v2[i]-expected_values[k2][i])**2)/expected_values[k2][i]
            #print(chi_statistics)
            mpc+=v2[i]
        p_value=1-chi2.cdf(x=chi_statistics,df=2)
        if (p_value<0.01): 
            outlier = 1
        else:
            outlier = 0
        air_data.append([k1,k2,mpc/3,p_value,outlier])
# air_data


# %%
df= pd.DataFrame(air_data,columns=['State','Year','Mpc','p-value','outlier'])
# df


# %%
df.to_csv("../datasets/Air_Quality_chiscore.csv",index=False)


# %%
state_co=pd.read_csv('../datasets/State-Coordinates.csv')
# state_co


# %%
air_quality_map=pd.merge(df,state_co,on='State')
# air_quality_map


# %%
air_quality_map.to_csv("../datasets/ChiScore_MapFile.csv",index=False)


# %%
df[df['Year']=='2014']


# %%



# %%



# %%



