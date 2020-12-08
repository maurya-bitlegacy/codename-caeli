# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import csv
import json
import statistics 
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# %%
with open('../datasets/neighbors.csv', newline='') as f:
    reader = csv.reader(f)
    neighbor_list = list(reader)
# neighbor_list


# %%
len(neighbor_list)


# %%
neighbor={}
for i in range(1,34):
    neighbor[neighbor_list[i][0]]=neighbor_list[i][1:]
# neighbor


# %%
with open('../datasets/Final_Air_Quality_Data.csv', newline='') as f:
    reader = csv.reader(f)
    air_quality_list = list(reader)
# air_quality_list


# %%
air_quality_list=air_quality_list[1:]


# %%
air_quality_mpc={}
i=1
for ele in air_quality_list:
    air_quality_mpc[ele[0]]=air_quality_mpc.get(ele[0],{})
    l=[float(i) for i in ele[2:]]
    air_quality_mpc[ele[0]][ele[1]]= statistics.mean(l)
# air_quality_mpc


# %%
air_nbr_data=[]
for (k1,v1) in air_quality_mpc.items():
    for (k2,v2) in v1.items():
        nbr_mpc=[]
        # print(k1)
        for ele in neighbor[k1]:
            nbr_mpc.append(air_quality_mpc[ele][k2])
        if(len(nbr_mpc)<2):
            nbr_mean=round(nbr_mpc[0],3)
            nbr_std=round(0,3)
            zscore=round(0,3)
        else:
            nbr_mean=round(statistics.mean(nbr_mpc),3)
            nbr_std=round(statistics.stdev(nbr_mpc,nbr_mean),3)
            zscore = round((v2-nbr_mean)/nbr_std,3)
        if (v2>(nbr_mean+(nbr_std)/2)):
            spot = 1
        elif(v2<(nbr_mean-(nbr_std)/2)):
            spot = -1
        else:
            spot=0
        air_nbr_data.append([k1,k2,round(v2,3),zscore,spot])
# air_nbr_data


# %%
# neighbor['Puducherry']


# %%
df= pd.DataFrame(air_nbr_data,columns=['State','Year','Mpc','zscore','spot'])
# df


# %%
df.to_csv("../datasets/Air_Quality_Mpc_zscore.csv",index=False)


# %%
zscore_nbr=df.sort_values(['Year','zscore'],ascending=[True, False])
zscore_nbr.reset_index(drop=True,inplace=True)
# zscore_nbr


# %%
# zscore_nbr.head(33)


# %%
topSpots_df = pd.DataFrame(columns=['Year','spot','State1','State2','State3','State4','State5'])
i=0
while(i<320):
    hotstate_list=[]
    coldstate_list=[]
    hotstate = zscore_nbr[i:i+32].head(5)
    coldstate = zscore_nbr[i+27:i+32]
    year_id = str(int(hotstate.iloc[0]['Year']))
    hotstate_list=list(hotstate['State'])
    coldstate_list=list(coldstate['State'])
    topSpots_df=topSpots_df.append({'Year':year_id,'spot': 'hot','State1':hotstate_list[0],'State2':hotstate_list[1],'State3':hotstate_list[2],'State4':hotstate_list[3],'State5':hotstate_list[4]},ignore_index=True)
    topSpots_df=topSpots_df.append({'Year':year_id,'spot': 'cold','State1':coldstate_list[0],'State2':coldstate_list[1],'State3':coldstate_list[2],'State4':coldstate_list[3],'State5':coldstate_list[4]},ignore_index=True)  
    i+=32
# topSpots_df


# %%
topSpots_df.to_csv("../datasets/TopSpots.csv",index=False)


# %%
state_co=pd.read_csv('../datasets/State-Coordinates.csv')
# state_co


# %%
air_quality_map=pd.merge(df,state_co,on='State')
# air_quality_map


# %%
air_quality_map.to_csv("../datasets/Zscore_MapFile.csv",index=False)


# %%



# %%



