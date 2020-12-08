# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd 
import csv
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt 
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

state=[]
feature=[]
feature_total=[]
fea=[]
label_state=[]
year=['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
file = open("../datasets/MotorVehicles-UpdatedFormat.csv")
file_read = csv.reader(file, delimiter=',')
list_file=list(file_read)
for i in range(1,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        label_state.append(list_file[i][0])
        fea.append(list_file[i][2])
        name=list_file[i][0]
        feature=[]
        for j in range(i,len(list_file)):
            if name==list_file[j][0]:
                feature.append(float(list_file[j][2]))
            else:
                break
        feature_total.append(feature)
# print(feature_total)
# list(map(list, zip(*feature_total))) # short circuits at shortest nested list if table is jagged
# list(map(list, itertools.zip_longest(*feature_total, fillvalue=None))) # 

# feature_total = [[feature_total[j][i] for j in range(len(feature_total))] for i in range(len(feature_total[0]))] 
# print(feature_total)
label_year=year

fig, ax = plt.subplots(figsize=(28,28))
fig.suptitle('Heatmap Motor Vehicle', fontsize=18, y=1)

im = ax.imshow(feature_total, cmap='Greens')
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.20)

ax.set_xticks(np.arange(len(label_year)))
ax.set_yticks(np.arange(len(label_state)))

ax.set_xticklabels(label_year)
ax.set_yticklabels(label_state)

plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor")

for i in range(len(label_year)):
    for j in range(len(label_state)):
        c = feature_total[j][i]
        text = ax.text(i, j, str(c),
                       ha="center", va="center")
        ax.set_xticklabels(label_year)
        ax.set_yticklabels(label_state)

fig.tight_layout()

fig.colorbar(im, cax=cax, orientation='vertical')
plt.savefig("Heatmap Motor Vehicle.png")
# plt.show()


# %%
# import pandas as pd 
# import csv
# import numpy as np
# import seaborn as sns
# from matplotlib import pyplot as plt 
# from mpl_toolkits.axes_grid1 import make_axes_locatable

state=[]
feature=[]
feature_total=[]
fea=[]
label_state=[]
year=['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
file = open("../datasets/Industries-UpdatedFormat.csv")
file_read = csv.reader(file, delimiter=',')
list_file=list(file_read)
for i in range(1,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        label_state.append(list_file[i][0])
        fea.append(list_file[i][2])
        name=list_file[i][0]
        feature=[]
        for j in range(i,len(list_file)):
            if name==list_file[j][0]:
                feature.append(float(list_file[j][2]))
            else:
                break
        feature_total.append(feature)

label_year=year

fig, ax = plt.subplots(figsize=(28,28))
fig.suptitle('Heatmap Industries', fontsize=16, y=1)

im = ax.imshow(feature_total, cmap='Reds')
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.20)

ax.set_xticks(np.arange(len(label_year)))
ax.set_yticks(np.arange(len(label_state)))

ax.set_xticklabels(label_year)
ax.set_yticklabels(label_state)

plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor")

for i in range(len(label_year)):
    for j in range(len(label_state)):
        c = feature_total[j][i]
        text = ax.text(i, j, str(c),
                       ha="center", va="center")
        ax.set_xticklabels(label_year)
        ax.set_yticklabels(label_state)

fig.tight_layout()
fig.colorbar(im, cax=cax, orientation='vertical')
plt.savefig("Heatmap Industries.png")
# plt.show()


# %%
# import pandas as pd 
# import csv
# import numpy as np
# import seaborn as sns
# from matplotlib import pyplot as plt 
# from mpl_toolkits.axes_grid1 import make_axes_locatable

state=[]
feature=[]
feature_total=[]
label_state=[]
year=['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
file = open("../datasets/Final_Air_Quality_Data.csv")
file_read = csv.reader(file, delimiter=',')
list_file=list(file_read)
for i in range(1,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        label_state.append(list_file[i][0])
        name=list_file[i][0]
        feature=[]
        for j in range(i,len(list_file)):
            if name==list_file[j][0]:
                feature.append(float(list_file[j][2]))
            else:
                break
        feature_total.append(feature)

label_year=year

fig, ax = plt.subplots(figsize=(28,28))
fig.suptitle('Heatmap SO2 Concentration', fontsize=16, y=1)

im = ax.imshow(feature_total, cmap='Reds')
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.20)

ax.set_xticks(np.arange(len(label_year)))
ax.set_yticks(np.arange(len(label_state)))

ax.set_xticklabels(label_year)
ax.set_yticklabels(label_state)

plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor")

for i in range(len(label_year)):
    for j in range(len(label_state)):
        c = feature_total[j][i]
        text = ax.text(i, j, str(c)[0:7],
                       ha="center", va="center")
        ax.set_xticklabels(label_year)
        ax.set_yticklabels(label_state)

fig.tight_layout()

fig.colorbar(im, cax=cax, orientation='vertical')
plt.savefig("Heatmap SO2 Concentration.png")
# plt.show()


# %%
# import pandas as pd 
# import csv
# import numpy as np
# import seaborn as sns
# from matplotlib import pyplot as plt 
# from mpl_toolkits.axes_grid1 import make_axes_locatable


state=[]
feature=[]
feature_total=[]
label_state=[]
year=['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
# file = open("../output_datasets/Final_Air_Quality_Data.csv")
# file_read = csv.reader(file, delimiter=',')
# list_file=list(file_read)
for i in range(1,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        label_state.append(list_file[i][0])
        name=list_file[i][0]
        feature=[]
        for j in range(i,len(list_file)):
            if name==list_file[j][0]:
                feature.append(float(list_file[j][3]))
            else:
                break
        feature_total.append(feature)

label_year=year

fig, ax = plt.subplots(figsize=(28,28))
fig.suptitle('Heatmap NO2 Concentration', fontsize=16, y=1)

im = ax.imshow(feature_total, cmap='Blues')
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.20)

ax.set_xticks(np.arange(len(label_year)))
ax.set_yticks(np.arange(len(label_state)))

ax.set_xticklabels(label_year)
ax.set_yticklabels(label_state)

plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor")

for i in range(len(label_year)):
    for j in range(len(label_state)):
        c = feature_total[j][i]
        text = ax.text(i, j, str(c)[0:5],size=16,ha="center", va="center")
        ax.set_xticklabels(label_year)
        ax.set_yticklabels(label_state)

fig.tight_layout()

fig.colorbar(im, cax=cax, orientation='vertical')
plt.savefig("Heatmap NO2 Concentration.png")
# plt.show()


# %%
# import pandas as pd 
# import csv
# import numpy as np
# import seaborn as sns
# from matplotlib import pyplot as plt 
# from mpl_toolkits.axes_grid1 import make_axes_locatable


state=[]
feature=[]
feature_total=[]
label_state=[]
year=['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
# file = open("../output_datasets/Final_Air_Quality_Data.csv")
# file_read = csv.reader(file, delimiter=',')
# list_file=list(file_read)
for i in range(1,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        label_state.append(list_file[i][0])
        name=list_file[i][0]
        feature=[]
        for j in range(i,len(list_file)):
            if name==list_file[j][0]:
                feature.append(float(list_file[j][4]))
            else:
                break
        feature_total.append(feature)
label_year=year

fig, ax = plt.subplots(figsize=(28,28))
fig.suptitle('Heatmap RSPM Concentration', fontsize=16, y=1)

im = ax.imshow(feature_total, cmap='Oranges')
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.20)

ax.set_xticks(np.arange(len(label_year)))
ax.set_yticks(np.arange(len(label_state)))

ax.set_xticklabels(label_year)
ax.set_yticklabels(label_state)

plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor")

for i in range(len(label_year)):
    for j in range(len(label_state)):
        c = feature_total[j][i]
        text = ax.text(i, j, str(c)[0:5],size=16,
                       ha="center", va="center")
        ax.set_xticklabels(label_year)
        ax.set_yticklabels(label_state)

fig.tight_layout()

fig.colorbar(im, cax=cax, orientation='vertical')
plt.savefig("Heatmap RSPM Concentration.png")
# plt.show()


# %%
# import pandas as pd 
# import csv
# import numpy as np
# import seaborn as sns
# from matplotlib import pyplot as plt 
# from mpl_toolkits.axes_grid1 import make_axes_locatable


# state=[]
# feature=[]
# feature_total=[]
# label_state=[]

# year=['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
# file = open("../datasets/pop_density.csv")
# file_read = csv.reader(file, delimiter=',')
# list_file=list(file_read)

    
# for i in range(1,len(list_file)):
#     feature=[]
#     if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
#         continue
#     else:
#         state.append(list_file[i][0])
#         for j in range (1,11):
#             feature.append(float(list_file[i][j])/float(list_file[i][11]))
#     feature_total.append(feature)
# # print(feature_total)
# label_year=year

# fig, ax = plt.subplots(figsize=(28,28))
# fig.suptitle('Heatmap Population Density', fontsize=16, y=1)

# im = ax.imshow(feature_total, cmap='Oranges')
# divider = make_axes_locatable(ax)
# cax = divider.append_axes('right', size='5%', pad=1)

# ax.set_xticks(np.arange(len(label_year)))
# ax.set_yticks(np.arange(len(state)))
    
# ax.set_xticklabels(label_year)
# ax.set_yticklabels(state)

# plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
#          rotation_mode="anchor")

# for i in range(len(label_year)):
#     for j in range(len(state)):
#         c = feature_total[j][i]
#         text = ax.text(i, j, str(c)[0:10],
#                        ha="center", va="center")
#         ax.set_xticklabels(label_year)
#         ax.set_yticklabels(state)

# fig.tight_layout()

# fig.colorbar(im, cax=cax, orientation='vertical')
# plt.savefig("Heatmap Population Density_old.png")
# # plt.show()


# %%
import pandas as pd 
import csv
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt 
from mpl_toolkits.axes_grid1 import make_axes_locatable


state=[]
feature=[]
feature_total=[]
label_state=[]

year=['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
file = open("../datasets/Population_density_final.csv")
file_read = csv.reader(file, delimiter=',')
list_file=list(file_read)

i = 1
#print(len(list_file))
while i<len(list_file):
    feature=[]
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        i = i+1
        continue
    else:
        state.append(list_file[i][0])
        for j in range (0,10):
            #print(i+j)
            feature.append(round(float(list_file[i+j][2]),1))
            
            
    i = i + j + 1
    feature_total.append(feature)

label_year=year
#print(feature_total)

fig, ax = plt.subplots(figsize=(28,28))
fig.suptitle('Heatmap for Population Density', fontsize=18, y=1)

im = ax.imshow(feature_total, cmap='Oranges')
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='10%', pad=0.20)
cax.tick_params(labelsize = 16)

ax.set_xticks(np.arange(len(label_year)))
ax.set_yticks(np.arange(len(state)))
    
ax.set_xticklabels(label_year, weight = 'bold')
ax.set_yticklabels(state, weight = 'bold')

plt.setp(ax.get_xticklabels(), rotation=90, ha="right",
         rotation_mode="anchor")

for i in range(len(label_year)):
    for j in range(len(state)):
        c = feature_total[j][i]
        text = ax.text(i, j, str(c)[0:10],
                       ha="center", va="center", size = 16)
        ax.set_xticklabels(label_year)
        ax.set_yticklabels(state)
        ax.set_label
ax.set_ylabel('State', fontsize=20)
ax.set_xlabel('Year', fontsize=20)

fig.tight_layout()

fig.colorbar(im, cax=cax, orientation='vertical')
plt.savefig("Heatmap for Population Density.png")
# plt.show()


# %%
# import csv
# from matplotlib import pyplot as plt 
# import pandas as pd 


state_feature={}

file = open("../datasets/MotorVehicles-UpdatedFormat.csv")
file_read = csv.reader(file, delimiter=',')
list_file=list(file_read)

for i in range(10,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        state_feature[list_file[i][0]]=float(list_file[i][2])


temp=dict(sorted(state_feature.items(),key=lambda item:item[1],reverse=True))
fig= plt.subplots(figsize=(15,15))
plt.bar(list(temp.keys()),list(temp.values()))
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel('Number of Motor Vehicles')
plt.title('State vs Number of Motor vehicles')
plt.savefig('State vs Motor vehicles.png')
# plt.show()


# %%
# import csv
# from matplotlib import pyplot as plt 
# import pandas as pd 


state_feature={}

file = open("../datasets/Industries-UpdatedFormat.csv")
file_read = csv.reader(file, delimiter=',')
list_file=list(file_read)

for i in range(10,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        state_feature[list_file[i][0]]=float(list_file[i][2])

temp=dict(sorted(state_feature.items(),key=lambda item:item[1],reverse=True))
fig= plt.subplots(figsize=(15,15))
plt.bar(list(temp.keys()),list(temp.values()))
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel('Number of Industries')
plt.title('State vs Number of Industries')
plt.savefig('State vs Industries.png')
# plt.show()


# %%
# import csv
# from matplotlib import pyplot as plt 
# import pandas as pd 


state_feature={}

file = open("../datasets/Final_Air_Quality_Data.csv")
file_read = csv.reader(file, delimiter=',')
list_file=list(file_read)

for i in range(10,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        state_feature[list_file[i][0]]=float(list_file[i][2])
temp=dict(sorted(state_feature.items(),key=lambda item:item[1],reverse=True))
fig= plt.subplots(figsize=(15,15))
plt.bar(list(temp.keys()),list(temp.values()))
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel('SO2 Concentration')
plt.title('State vs SO2')
plt.savefig('State vs SO2')
# plt.show()


# %%
# import csv
# from matplotlib import pyplot as plt 
# import pandas as pd 


state_feature={}

# file = open("../output_datasets/Final_Air_Quality_Data.csv")
# file_read = csv.reader(file, delimiter=',')
# list_file=list(file_read)

for i in range(10,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        state_feature[list_file[i][0]]=float(list_file[i][3])

temp=dict(sorted(state_feature.items(),key=lambda item:item[1],reverse=True))
fig= plt.subplots(figsize=(15,15))
plt.bar(list(temp.keys()),list(temp.values()))
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel('NO2 concentration')
plt.title('State vs NO2')
plt.savefig('State vs NO2.png')
# plt.show()


# %%
# import csv
# from matplotlib import pyplot as plt 
# import pandas as pd 


state_feature={}

# file = open("../output_datasets/Final_Air_Quality_Data.csv")
# file_read = csv.reader(file, delimiter=',')
# list_file=list(file_read)

for i in range(10,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        state_feature[list_file[i][0]]=float(list_file[i][4])

temp=dict(sorted(state_feature.items(),key=lambda item:item[1],reverse=True))
fig= plt.subplots(figsize=(15,15))
plt.bar(list(temp.keys()),list(temp.values()))
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel('RSPM Concentration')
plt.title('State vs rspm')
plt.savefig('State vs rspm.png')
# plt.show()


# %%
# import csv
# from matplotlib import pyplot as plt 
# import pandas as pd 


state_feature={}

file = open("../datasets/Population_density_final.csv")
file_read = csv.reader(file, delimiter=',')
list_file=list(file_read)

for i in range(10,len(list_file),10):
    if list_file[i][0]=='Arunachal Pradesh' or list_file[i][0]=='Sikkim' or list_file[i][0]=='Dadra & Nagar Haveli' or list_file[i][0]=='Daman & Diu':
        continue
    else:
        state_feature[list_file[i][0]]=float(list_file[i][2])
fig= plt.subplots(figsize=(15,15))
temp=dict(sorted(state_feature.items(),key=lambda item:item[1],reverse=True))
plt.bar(list(temp.keys()),list(temp.values()))
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel('Population per sq. km')
plt.title('State vs Population density')
plt.savefig('State vs Population Density.png')
# plt.show()


