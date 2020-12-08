# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import csv
from bs4 import BeautifulSoup
import requests
import xlrd
import json
import math
from scipy import interpolate
import warnings
warnings.simplefilter(action='ignore')
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))


# %%
#CLEAN AIR QUALITY FROM RAW DATA

inputfile  = '../datasets/data.csv'
outputfile = "../datasets/AirQualityData-Clean.csv"
df = pd.read_csv(inputfile, encoding = "ISO-8859-1")

df = df.drop(['stn_code', 'sampling_date', 'agency', 'type', 'location_monitoring_station','pm2_5', 'spm'], axis = 1)

years = ['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
df = df[df["date"].str.contains('|'.join(years), na=False)]
df.loc[:, 'date'] = df['date'].str.split('-', expand=True)[0]

df['state'] = df['state'].replace(['Uttaranchal'],'Uttarakhand')
df = df.groupby(['state','date']).mean()
df.loc[('Telangana', '2014')] = df.loc[[('Andhra Pradesh', '2014'), ('Telangana', '2014')]].sum()
df = df.drop(('Telangana', '2014'))

df.to_csv(outputfile)


# %%
#CLEAN INDUSTRIES FROM RAW DATA

inputfile  = '../datasets/Industries.xlsx'
outputfile = "../datasets/Industries-Clean.csv"
df = pd.read_excel(inputfile, sheet_name='State-wise')

df = df.iloc[:, :7]             # only include columns from start till 7th index in df
df.iloc[7,0] = 'state/ut'       # assign first column header  
df.iloc[7] = [(word[0:2]+word[-2:]).strip() for word in df.iloc[7]] # change '2011-12' to '2012'
df.iloc[7,0] = 'state/ut'       # assign first column header  
new_header = df.iloc[7]         #grab the fourth row for the header
df = df[10:46]                  #take the data less the header row
df.columns = new_header         #set the header row as the df header

df = df.drop([df.index[28]]) 
df.iloc[:, :].replace({'-': None}, inplace=True) # replace - with None/Null

df = df.set_index("state/ut")
df = df.rename(index={'A & N. Island': 'Andaman & Nicobar Islands'})
df = df.rename(index={'Dadra & N Haveli': 'Dadra & Nagar Haveli'})
df = df.rename(index={'UttaraKhand': 'Uttarakhand'})
df.loc['Andhra Pradesh', :] = df.loc[['Andhra Pradesh', 'Telangana']].sum()
df = df.drop('Telangana')

df.to_csv(outputfile)


# %%
#CLEAN MOTOR VEHICLES FROM RAW DATA

inputfile  = '../datasets/MotorVehicles.xlsx'
outputfile = "../datasets/MotorVehicles-Clean.csv"
df = pd.read_excel(inputfile)

df.iloc[4,0] = 'state/ut'
df.iloc[4] = [str(word).strip() for word in df.iloc[4]]
new_header = df.iloc[4] #grab the fourth row for the header
df = df[8:46] #take the data less the header row
df.columns = new_header #set the header row as the df header

df = df.drop([df.index[29], df.index[30]])
df.iloc[:, :].replace({'-': None}, inplace=True) # replace - with None/Null

# Remove white spaces
df["state/ut"] = df["state/ut"].str.strip()

df = df.set_index("state/ut")

df = df.rename(index={'Orissa': 'Odisha'})
df = df.rename(index={'Chhatisgarh': 'Chhattisgarh'})
df = df.rename(index={'A. & N. Islands': 'Andaman & Nicobar Islands'})
df = df.rename(index={'D. & N. Haveli': 'Dadra & Nagar Haveli'})

idx = df[~df.iloc[:, 1:].applymap(np.isreal).all(1)].index #index having non numeric values
for i in df.index:
    for c in df.columns:
        if type(df[c][i]) == str:
            
            k = len(df[c][i]) - 1
            while(k >= 0):
                if not df[c][i][k].isdigit():
                    df[c][i] = df[c][i][:k] + df[c][i][k+1:]
                k-=1
            df[c][i] = int(df[c][i])
            
df.loc['Andhra Pradesh', :] = df.loc[['Andhra Pradesh', 'Telangana']].sum()
df = df.drop('Telangana')

df.to_csv(outputfile)


# %%
#CHANGE FORMAT OF INDUSTRIES AND MOTOR VEHICLES

def correctFormat(inputfile, inputfile2, outputfile):
    with open(inputfile, 'r') as f:
        ip = list(csv.reader(f))

        if outputfile.startswith('../datasets/Industries'):
            with open(inputfile2, 'r') as f:
                ip2 = list(csv.reader(f))

            for i in range(len(ip2)):
                for col in range(1, 7):
                    ip[i].append(ip2[i][col])
    
    op = [['State', 'Year', 'Feature']]

    for row in ip[1:]:
        for col in range(5,15):
            if row[0] not in ['Andaman & Nicobar Islands', 'Lakshadweep', 'Tripura']:
                if len(row) == 0 or len(ip[0]) == 0:
                    continue
                op.append([row[0], ip[0][col], row[col]])
    
    with open(outputfile, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(op)


inputfile = '../datasets/2001-2008_industry_data_CLEANED.csv'
outputfile = '../datasets/Industries-UpdatedFormat.csv'
inputfile2 = '../datasets/Industries-Clean.csv'
correctFormat(inputfile, inputfile2, outputfile)

inputfile = '../datasets/MotorVehicles-Clean.csv'
outputfile = '../datasets/MotorVehicles-UpdatedFormat.csv'
correctFormat(inputfile, '', outputfile)


# %%
#SCRAPE 2001 POPULATION DATA

dict_population={}
temp_pop=[]
temp_state=[]
temp_state_name=[]
result=[]
BASE_URL = "https://censusindia.gov.in/Census_Data_2001/Census_data_finder/A_Series/Total_population.htm"
html = requests.get(BASE_URL, verify=False).text
soup = BeautifulSoup(html, "html.parser")
tds = soup.find_all(class_='xl296353')
tds_pop = soup.find_all(class_='xl306353')
for td in tds_pop:
    if td.text!='\xa0' :
       temp_pop.append(td.text)

for i in range(0,len(temp_pop),3):
    temp_state.append(temp_pop[i])

for td in tds:
    if td.text!='\xa0' :
       temp_state_name.append(td.text)


# print(temp_state)
for i in range(0,len(temp_state_name)):
    if temp_state_name[i]=='Andaman &\r\n  Nicobar Islands' or temp_state_name[i]=='Lakshadweep' or temp_state_name[i]=='Tripura':
        continue
    else:
        if "\r\n " in temp_state_name[i]:
            res=temp_state_name[i].replace("\r\n ","")
            dict_population[res]=float(temp_state[i].replace(',',''))
        elif temp_state_name[i]=="Orissa":
            res= temp_state_name[i].replace("Orissa","Odisha")
            dict_population[res]=float(temp_state[i].replace(',',''))
        elif temp_state_name[i]=="Uttaranchal":
            res= temp_state_name[i].replace("Uttaranchal","Uttarakhand")
            dict_population[res]=float(temp_state[i].replace(',',''))
        elif temp_state_name[i]=="Pondicherry":
            res= temp_state_name[i].replace("Pondicherry","Puducherry")
            dict_population[res]=float(temp_state[i].replace(',',''))
        elif temp_state_name[i]=="Manipur*":
            res= temp_state_name[i].rstrip('*')
            dict_population[res]=float(temp_state[i].replace(',',''))
        else:
            dict_population[temp_state_name[i]]=float(temp_state[i].replace(',',''))

r=sorted(dict_population.items())
for ele in r:
    result.append({'State/UT':ele[0],'Population':ele[1]})
# print(result)
with open('../datasets/2001_population.json', 'w') as fp:
    json.dump(dict_population, fp)

try:
    with open("../datasets/2001_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result)
except IOError:
    print("I/O error")


# %%
#SCRAPE 2011 POPULATION DATA

pop_2011={}
result=[]
wb = xlrd.open_workbook('../datasets/Table 2.1_4.xls')
sh = wb.sheet_by_name("Table 2.1")

for i in range(8,45):
    cell_value_pop = sh.cell(i,4).value
    cell_value_state = sh.cell(i,0).value
    cell_value_area = sh.cell(i,1).value
    if cell_value_pop=="" or cell_value_state==' A.& N.Islands ' or cell_value_state==' Lakshadweep ' or cell_value_state==' Tripura':
    	continue	
    else:
        if cell_value_state==" D.& N.Haveli ":
            res=cell_value_state.replace(" D.& N.Haveli ","Dadra & Nagar Haveli")
        # elif cell_value_state==" Puducherry ":
        # 	res=cell_value_state.replace(" Puducherry ","Pondicherry")

        elif cell_value_state==" Jammu & Kashmir (1) ++":
            res=cell_value_state.replace(" Jammu & Kashmir (1) ++","Jammu & Kashmir")
        else:
            res=cell_value_state.strip()
        pop_2011[res] = {'Population':cell_value_pop,'Area': cell_value_area}

sort_final=sorted(pop_2011.items())
for ele in sort_final:
    arr=[]
    for value in ele[1].values():
        arr.append(value)
    result.append({'State/UT':ele[0],'Population':arr[0],'Area':arr[1]})
# print(result)
with open('../datasets/2011_population.json', 'w') as fp:
    json.dump(pop_2011, fp)
try:
    with open("../datasets/2011_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population','Area'])
        writer.writeheader()
        writer.writerows(result)
except IOError:
    print("I/O error")


# %%
#CONVERT POPULATION JSON TO CSV

pop_2002={}
result_2002=[]
with open('../datasets/2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('../datasets/2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1
    pop_2002[key]=data_2001[key]*(1+rate)
r=sorted(pop_2002.items())
for ele in r:
    result_2002.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2002_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2002)
except IOError:
    print("I/O error")
  
#2003_data
pop_2003={}
result_2003=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1
    pop_2003[key]=data_2001[key]*(1+rate)**2
r=sorted(pop_2003.items())
for ele in r:
    result_2003.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2003_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2003)
except IOError:
    print("I/O error")
#2004_data
pop_2004={}
result_2004=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1
    pop_2004[key]=data_2001[key]*(1+rate)**3
r=sorted(pop_2004.items())
for ele in r:
    result_2004.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2004_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2004)
except IOError:
    print("I/O error")
    
#2005_data
pop_2005={}
result_2005=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1

    pop_2005[key]=data_2001[key]*(1+rate)**4
r=sorted(pop_2005.items())
for ele in r:
    result_2005.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2005_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2005)
except IOError:
    print("I/O error")

#2006_data
pop_2006={}
result_2006=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1
    # print(rate)

    pop_2006[key]=data_2001[key]*(1+rate)**5

r=sorted(pop_2006.items())
for ele in r:
    result_2006.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2006_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2006)
except IOError:
    print("I/O error")

#2007_data
pop_2007={}
result_2007=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1
    pop_2007[key]=data_2001[key]*(1+rate)**6
r=sorted(pop_2007.items())
for ele in r:
    result_2007.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2007_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2007)
except IOError:
    print("I/O error")

#2008_data
pop_2008={}
result_2008=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1
    pop_2008[key]=data_2001[key]*(1+rate)**7
r=sorted(pop_2008.items())
for ele in r:
    result_2008.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2008_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2008)
except IOError:
    print("I/O error")

#2009_data    
pop_2009={}
result_2009=[]
pop_keys_2011=data_2011.keys()

for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1
    pop_2009[key]=data_2001[key]*(1+rate)**8
r=sorted(pop_2009.items())
for ele in r:
    result_2009.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2009_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2009)
except IOError:
    print("I/O error")

#2010_data
pop_2010={}
result_2010=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    rate=pow(10,l)-1
    pop_2010[key]=data_2001[key]*(1+rate)**9
r=sorted(pop_2010.items())
for ele in r:
    result_2010.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2010_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2010)
except IOError:
    print("I/O error")
    
#2012_data
pop_2012={}
result_2012=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    rate=pow(10,l)-1
    pop_2012[key]=data_2001[key]*(1+rate)**11
r=sorted(pop_2012.items())
for ele in r:
    result_2012.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2012_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2012)
except IOError:
    print("I/O error")

#2013_data
pop_2013={}
result_2013=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    # print(l)
    rate=pow(10,l)-1
    # print(rate)

    pop_2013[key]=data_2001[key]*(1+rate)**12
r=sorted(pop_2013.items())
for ele in r:
    result_2013.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2013_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2013)
except IOError:
    print("I/O error")

#2014_data
pop_2014={}
result_2014=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    rate=pow(10,l)-1
    pop_2014[key]=data_2001[key]*(1+rate)**13
r=sorted(pop_2014.items())
for ele in r:
    result_2014.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2014_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2014)
except IOError:
    print("I/O error")

#2015_data
pop_2015={}
result_2015=[]
pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
    l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
    rate=pow(10,l)-1
    pop_2015[key]=data_2001[key]*(1+rate)**14

r=sorted(pop_2015.items())
for ele in r:
    result_2015.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
    with open("../datasets/2015_population.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
        writer.writeheader()
        writer.writerows(result_2015)
except IOError:
    print("I/O error")


# %%
#MERGE POPULATION DATA OF ALL YEARS

with open('../datasets/2011_population.json') as f:
  data = json.load(f)

area = {}

for x in data:
	for y in data[x]:
		if y == 'Area':
			area[x] = data[x][y]

final = {}

with open("../datasets/2005_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]] = [line[1]]

with open("../datasets/2006_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("../datasets/2007_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("../datasets/2008_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("../datasets/2009_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("../datasets/2010_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("../datasets/2011_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("../datasets/2012_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("../datasets/2013_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("../datasets/2014_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])


res = []
i = 2005

for x in final:
	for y in final[x]:
		if x == 'State/UT':
			continue
		temp = [x,i]
		i+=1
		if i==2015:
			i = 2005
		ar = float(area[x])
		y = float(y)
		y = round(y/ar,4)
		temp.append(y)
		res.append(temp)


with open('../datasets/Population_density_final.csv', 'w', newline='') as file:
	wr = csv.writer(file)#,  delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	wr.writerow(['State/UT', 'Year', 'Population_density'])
	for x in res:
		wr.writerow(x)


# %%
#ADD MISSING VALUES USING INTERPOLATION

article_open= open('../datasets/AirQualityData-Clean.csv')
csv_read = csv.reader(article_open)
list_csv=list(csv_read)

dict_data={}
list_state=[]
for i in range(1,len(list_csv)):
    dict_data[list_csv[i][0]+'/'+list_csv[i][1]]=list_csv[i][2:]
    list_state.append(list_csv[i][0])
# print(dict_data)    

for state in list(set(list_state)):
    year_so2=[]
    year_no2=[]
    year_rspm=[]
    empty_year_so2=[]
    empty_year_no2=[]
    empty_year_rspm=[]
    value_so2=[]
    value_no2=[]
    value_rspm=[]
    for i, j in dict_data.items():
        temp=i.split('/')
        if temp[0]==state:
            if j[0]!='':
                year_so2.append(int(temp[1]))
                value_so2.append(float(j[0]))
                
            else:
                empty_year_so2.append(int(temp[1]))
            
            if j[1]!='':
                year_no2.append(int(temp[1]))
                value_no2.append(float(j[1]))
            else:
                empty_year_no2.append(int(temp[1]))
            if j[2]!='':
                year_rspm.append(int(temp[1]))
                value_rspm.append(float(j[2]))
            else:
                empty_year_rspm.append(int(temp[1]))
#     print(empty_year_so2)
    for y in empty_year_so2:
#         print(y)
        stats= dict_data[state+'/'+str(y)]
        s = interpolate.interp1d(year_so2, value_so2, kind='linear',fill_value='extrapolate')
        stats[0]=str(s(y))
        dict_data[state+'/'+str(y)]=stats
        
    for y in empty_year_no2:
        # print(y)
        stats= dict_data[state+'/'+str(y)]    
        n = interpolate.interp1d(year_no2, value_no2, kind='linear', fill_value = "extrapolate")
        stats[1]=str(n(y))
        dict_data[state+'/'+str(y)]=stats
        
    for y in empty_year_rspm:
        stats= dict_data[state+'/'+str(y)]
        r = interpolate.interp1d(year_rspm, value_rspm, kind='linear', fill_value = "extrapolate")
        stats[2]=str(r(y))
        dict_data[state+'/'+str(y)]=stats
        
# print(dict_data)       

state_array=['Assam','Bihar','Dadra & Nagar Haveli','Daman & Diu','Delhi','Jammu & Kashmir','Karnataka','Meghalaya','Mizoram','Nagaland','Uttarakhand']

for state in state_array:
    year=[]
    value_so2=[]
    value_no2=[]
    value_rspm=[]
    for i,j in dict_data.items():
        temp=i.split('/')
        if temp[0]==state:
            year.append(int(temp[1]))
            value_so2.append(float(j[0]))           
            value_no2.append(float(j[1]))       
            value_rspm.append(float(j[2]))
                          
    for y in range(2005,2015):
        stats=[]
        if y not in year:
            s = interpolate.interp1d(year, value_so2, kind='linear',fill_value = "extrapolate")
            n = interpolate.interp1d(year, value_no2, kind='linear',fill_value = "extrapolate")
            r = interpolate.interp1d(year, value_rspm, kind='linear',fill_value = "extrapolate")
            stats.append(str(s(y)))
            stats.append(str(n(y)))
            stats.append(str(r(y))) 
            dict_data[state+'/'+str(y)]=stats

# print(dict_data)

result=[]
final=dict(sorted(dict_data.items())) 
for i,j in final.items():
    temp=i.split('/')
    result.append({'State':temp[0],'Year':temp[1],'so2':j[0],'no2':j[1],'rspm':j[2]})


try:
    with open("../datasets/filled_data_air.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['State', 'Year','so2','no2','rspm'])
        writer.writeheader()
        writer.writerows(result)
except IOError:
    print("I/O error")

#lagranges method-bihar
x=np.array([2005,2006,2007,2008,2009,2010,2011,2012],float)
y=np.array([103.38805970149254,111.0828402366864,116.36216216216216,118.65441176470588,98.4776119402985,165.28057553956833,158.03030303030303,161.66390041493776],float)

x13=2013
x14=2014

y13=0
y14=0

for xi,yi in zip(x,y):
   y13+=yi*np.prod((x13-x[x != xi])/(xi-x[x != xi])) 
# print(x13,y13)

for xi,yi in zip(x,y):
   y14+=yi*np.prod((x14-x[x != xi])/(xi-x[x != xi])) 
# print(x14,y14)

# cubic interpolation for bihar 
from scipy.interpolate import interp1d 

x = [2005,2006,2007,2008,2009,2010,2011,2012]
y = [103.38805970149254,111.0828402366864,116.36216216216216,118.65441176470588,98.4776119402985,165.28057553956833,158.03030303030303,161.66390041493776]

# xx = [1,2,3,4,5,6,7,8,9,10,11,12] 
f = interp1d(x, y, kind='cubic',fill_value='extrapolate') 

# print(f(2013))
# print(f(2014))

# quadratic interpolation for bihar
from scipy.interpolate import interp1d 

x = [2005,2006,2007,2008,2009,2010,2011,2012]
y = [103.38805970149254,111.0828402366864,116.36216216216216,118.65441176470588,98.4776119402985,165.28057553956833,158.03030303030303,161.66390041493776]

# xx = [1,2,3,4,5,6,7,8,9,10,11,12] 
f = interp1d(x, y, kind='quadratic',fill_value='extrapolate') 

# print(f(2013))
# print(f(2014))

from scipy.interpolate import interp1d 

x = [2005,2006,2007,2008,2009,2010,2011,2012]
y = [103.38805970149254,111.0828402366864,116.36216216216216,118.65441176470588,98.4776119402985,165.28057553956833,158.03030303030303,161.66390041493776]

# xx = [1,2,3,4,5,6,7,8,9,10,11,12] 
f = interp1d(x, y, kind='linear',fill_value='extrapolate') 

# print(f(2013))
# print(f(2014))

# linear vs quadratic interpolation graph for bihar
from scipy.interpolate import interp1d 
import numpy as np
x = [2005,2006,2007,2008,2009,2010,2011,2012]
y = [103.38805970149254,111.0828402366864,116.36216216216216,118.65441176470588,98.4776119402985,165.28057553956833,158.03030303030303,161.66390041493776]

# xx = [1,2,3,4,5,6,7,8,9,10,11,12] 
xnew = np.linspace(2003, 2014, num=41, endpoint=True)
f = interp1d(x, y, kind='linear',fill_value='extrapolate') 
f2 = interp1d(x, y, kind='quadratic',fill_value='extrapolate') 
import matplotlib.pyplot as plt
temp=f(2013)
# plt.plot(x,y,'o',ms=6)
# plt.plot(x,y)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
# plt.show()
# print("linear")
# print(f(2004))
# print(f(2013))
# print(f(2014))

# print("Quadratic")
# print(f2(2004))
# print(f2(2013))
# print(f2(2014))


# linear vs quadratic interpolation for nagaland
from scipy.interpolate import interp1d 
import numpy as np
x = [2005,2006,2007,2008,2009,2010,2011,2013]
y = [79.76470588235294,72.98584905660377,67.4423076923077,72.38425925925925,79.4888888888889,72.44244604316546,82.34134615384616,92.78643216080403]

# xx = [1,2,3,4,5,6,7,8,9,10,11,12] 
xnew = np.linspace(2003, 2014, num=41, endpoint=True)
f = interp1d(x, y, kind='linear',fill_value='extrapolate') 
f2 = interp1d(x, y, kind='quadratic',fill_value='extrapolate') 
import matplotlib.pyplot as plt
temp=f(2013)
# plt.plot(x,y,'o',ms=6)
# plt.plot(x,y)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
# plt.show()
# print("linear")

# print(f(2012))
# print(f(2014))

# print("Quadratic")

# print(f2(2012))
# print(f2(2014))

# linear vs quadratic interpolation for uttarakhand
from scipy.interpolate import interp1d 
import numpy as np
x = [2005,2006,2007,2008,2010,2011,2012,2013]
y = [	152.86206896551724,120.37931034482759,100.27380952380952,124.63888888888889,151.41368749575003,159.7810292855297,180.41585526315788,141.8446153846154]

# xx = [1,2,3,4,5,6,7,8,9,10,11,12] 
xnew = np.linspace(2003, 2014, num=41, endpoint=True)
f = interp1d(x, y, kind='linear',fill_value='extrapolate') 
f2 = interp1d(x, y, kind='quadratic',fill_value='extrapolate') 
import matplotlib.pyplot as plt
temp=f(2013)
# plt.plot(x,y,'o',ms=6)
# plt.plot(x,y)
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
# plt.show()
# print("linear")

# print(f(2012))
# print(f(2014))

# print("Quadratic")

# print(f2(2012))
# print(f2(2014))


# %%
with open('../datasets/neighbors.csv', newline='') as f:
    reader = csv.reader(f)
    neighbors = list(reader)

sikkim_neighbor=[]
manipur_neighbor=[]
arunachal_neighbor=[]
for ele in neighbors:
    if ele[0]=='Sikkim':
        sikkim_neighbor=ele[1:]
    elif ele[0]=='Manipur':
        manipur_neighbor=ele[1:]
    elif ele[0]=='Arunachal Pradesh':
        arunachal_neighbor=ele[1:]

air_quality=pd.read_csv("../datasets/filled_data_air.csv")

#calculation to find ratio of so2,no2 & rspm for sikkim & west bengal 
sikkim_so2=list(air_quality[air_quality['State']=='Sikkim']['so2'])[0]
sikkim_no2=list(air_quality[air_quality['State']=='Sikkim']['no2'])[0]
sikkim_rspm=list(air_quality[air_quality['State']=='Sikkim']['rspm'])[0]

westBengal_so2=list(air_quality[(air_quality['State']=='West Bengal') & (air_quality['Year']==2007)]['so2'])[0]
westBengal_no2=list(air_quality[(air_quality['State']=='West Bengal') & (air_quality['Year']==2007)]['no2'])[0]
westBengal_rspm=list(air_quality[(air_quality['State']=='West Bengal') & (air_quality['Year']==2007)]['rspm'])[0]

sikkim_so2ratio=sikkim_so2/westBengal_so2
sikkim_no2ratio=sikkim_no2/westBengal_no2
sikkim_rspmratio=sikkim_rspm/westBengal_rspm

#values of so2 in WB for every year
westBengal_SO2=list(air_quality[(air_quality['State']=='West Bengal')]['so2'])

#finding values of so2 in sikkim for every year
sikkim_SO2=[]
for ele in westBengal_SO2:
    sikkim_SO2.append(ele*sikkim_so2ratio)

#values of no2 in WB for every year
westBengal_NO2=list(air_quality[(air_quality['State']=='West Bengal')]['no2'])

#finding values of no2 in sikkim for every year
sikkim_NO2=[]
for ele in westBengal_NO2:
    sikkim_NO2.append(ele*sikkim_no2ratio)
    
#values of rspm in WB for every year
westBengal_rspm=list(air_quality[(air_quality['State']=='West Bengal')]['rspm'])

#finding values of rspm in sikkim for every year
sikkim_rspm=[]
for ele in westBengal_rspm:
    sikkim_rspm.append(ele*sikkim_rspmratio)

missing_rows=[]
for i in range(0,10):
    if(i!=2):
        missing_rows.append(['Sikkim',2005+i,sikkim_SO2[i],sikkim_NO2[i],sikkim_rspm[i]])

air_quality[air_quality['State']=='Arunachal Pradesh']

arunachal_so2=list(air_quality[(air_quality['State']=='Arunachal Pradesh') & (air_quality['Year']==2014)]['so2'])[0]
arunachal_no2=list(air_quality[(air_quality['State']=='Arunachal Pradesh') & (air_quality['Year']==2014)]['no2'])[0]
arunachal_rspm=list(air_quality[(air_quality['State']=='Arunachal Pradesh') & (air_quality['Year']==2014)]['rspm'])[0]

assam_so2=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2014)]['so2'])[0]
assam_no2=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2014)]['no2'])[0]
assam_rspm=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2014)]['rspm'])[0]

nagaland_so2=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2014)]['so2'])[0]
nagaland_no2=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2014)]['no2'])[0]
nagaland_rspm=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2014)]['rspm'])[0]

arunachal_so2ratio1=arunachal_so2/assam_so2
arunachal_so2ratio2=arunachal_so2/nagaland_so2
arunachal_no2ratio1=arunachal_no2/assam_no2
arunachal_no2ratio2=arunachal_no2/nagaland_no2
arunachal_rspmratio1=arunachal_rspm/assam_rspm
arunachal_rspmratio2=arunachal_rspm/nagaland_rspm

#values of so2 in assam & nagaland for every year
assam_SO2=list(air_quality[(air_quality['State']=='Assam')]['so2'])
nagaland_SO2=list(air_quality[(air_quality['State']=='Nagaland')]['so2'])

#finding values of so2 in arunachal for every year
arunachal_SO2=[]
for i in range(0,10):
    val1=assam_SO2[i]*arunachal_so2ratio1
    val2=nagaland_SO2[i]*arunachal_so2ratio2
    arunachal_SO2.append((val1+val2)/2)

#values of no2 in assam & nagaland for every year
assam_NO2=list(air_quality[(air_quality['State']=='Assam')]['no2'])
nagaland_NO2=list(air_quality[(air_quality['State']=='Nagaland')]['no2'])

#finding values of no2 in arunachal for every year
arunachal_NO2=[]
for i in range(0,10):
    val1=assam_NO2[i]*arunachal_no2ratio1
    val2=nagaland_NO2[i]*arunachal_no2ratio2
    arunachal_NO2.append((val1+val2)/2)

#values of rspm in assam & nagaland for every year
assam_rspm=list(air_quality[(air_quality['State']=='Assam')]['rspm'])
nagaland_rspm=list(air_quality[(air_quality['State']=='Nagaland')]['rspm'])

#finding values of rspm in arunachal for every year
arunachal_rspm=[]
for i in range(0,10):
    val1=assam_rspm[i]*arunachal_rspmratio1
    val2=nagaland_rspm[i]*arunachal_rspmratio2
    arunachal_rspm.append((val1+val2)/2)

for i in range(0,9):
    missing_rows.append(['Arunachal Pradesh',2005+i,arunachal_SO2[i],arunachal_NO2[i],arunachal_rspm[i]])

air_quality[air_quality['State']=='Manipur']

manipur2007_so2=list(air_quality[(air_quality['State']=='Manipur') & (air_quality['Year']==2007)]['so2'])[0]
manipur2007_no2=list(air_quality[(air_quality['State']=='Manipur') & (air_quality['Year']==2007)]['no2'])[0]
manipur2007_rspm=list(air_quality[(air_quality['State']=='Manipur') & (air_quality['Year']==2007)]['rspm'])[0]
manipur2008_so2=list(air_quality[(air_quality['State']=='Manipur') & (air_quality['Year']==2008)]['so2'])[0]
manipur2008_no2=list(air_quality[(air_quality['State']=='Manipur') & (air_quality['Year']==2008)]['no2'])[0]
manipur2008_rspm=list(air_quality[(air_quality['State']=='Manipur') & (air_quality['Year']==2008)]['rspm'])[0]

air_quality[air_quality['State']=='Nagaland']

air_quality[air_quality['State']=='Mizoram']

air_quality[air_quality['State']=='Assam']

#values for nagaland 2007
nagaland_2007_so2=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2007)]['so2'])[0]
nagaland_2007_no2=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2007)]['no2'])[0]
nagaland_2007_rspm=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2007)]['rspm'])[0]

#values for nagaland 2008
nagaland_2008_so2=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2008)]['so2'])[0]
nagaland_2008_no2=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2008)]['no2'])[0]
nagaland_2008_rspm=list(air_quality[(air_quality['State']=='Nagaland') & (air_quality['Year']==2008)]['rspm'])[0]

#values for mizoram 2007
mizoram_2007_so2=list(air_quality[(air_quality['State']=='Mizoram') & (air_quality['Year']==2007)]['so2'])[0]
mizoram_2007_no2=list(air_quality[(air_quality['State']=='Mizoram') & (air_quality['Year']==2007)]['no2'])[0]
mizoram_2007_rspm=list(air_quality[(air_quality['State']=='Mizoram') & (air_quality['Year']==2007)]['rspm'])[0]

#values for mizoram 2008
mizoram_2008_so2=list(air_quality[(air_quality['State']=='Mizoram') & (air_quality['Year']==2008)]['so2'])[0]
mizoram_2008_no2=list(air_quality[(air_quality['State']=='Mizoram') & (air_quality['Year']==2008)]['no2'])[0]
mizoram_2008_rspm=list(air_quality[(air_quality['State']=='Mizoram') & (air_quality['Year']==2008)]['rspm'])[0]

#values for assam 2007
assam_2007_so2=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2007)]['so2'])[0]
assam_2007_no2=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2007)]['no2'])[0]
assam_2007_rspm=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2007)]['rspm'])[0]

#values for assam 2008
assam_2008_so2=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2008)]['so2'])[0]
assam_2008_no2=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2008)]['no2'])[0]
assam_2008_rspm=list(air_quality[(air_quality['State']=='Assam') & (air_quality['Year']==2008)]['rspm'])[0]

#ratios for 2007
manipur2007_so2ratio1=manipur2007_so2/nagaland_2007_so2
manipur2007_so2ratio2=manipur2007_so2/mizoram_2007_so2
manipur2007_so2ratio3=manipur2007_so2/assam_2007_so2

manipur2007_no2ratio1=manipur2007_no2/nagaland_2007_no2
manipur2007_no2ratio2=manipur2007_no2/mizoram_2007_no2
manipur2007_no2ratio3=manipur2007_no2/assam_2007_no2

manipur2007_rspmratio1=manipur2007_rspm/nagaland_2007_rspm
manipur2007_rspmratio2=manipur2007_rspm/mizoram_2007_rspm
manipur2007_rspmratio3=manipur2007_rspm/assam_2007_rspm

#ratios for 2008
manipur2008_so2ratio1=manipur2008_so2/nagaland_2008_so2
manipur2008_so2ratio2=manipur2008_so2/mizoram_2008_so2
manipur2008_so2ratio3=manipur2008_so2/assam_2008_so2

manipur2008_no2ratio1=manipur2008_no2/nagaland_2008_no2
manipur2008_no2ratio2=manipur2008_no2/mizoram_2008_no2
manipur2008_no2ratio3=manipur2008_no2/assam_2008_no2

manipur2008_rspmratio1=manipur2008_rspm/nagaland_2008_rspm
manipur2008_rspmratio2=manipur2008_rspm/mizoram_2008_rspm
manipur2008_rspmratio3=manipur2008_rspm/assam_2008_rspm

#finding mean ratios of 2007 & 2008
manipur_so2ratio1= (manipur2007_so2ratio1+manipur2008_so2ratio1)/2
manipur_so2ratio2= (manipur2007_so2ratio2+manipur2008_so2ratio2)/2
manipur_so2ratio3= (manipur2007_so2ratio3+manipur2008_so2ratio3)/2

manipur_no2ratio1= (manipur2007_no2ratio1+manipur2008_no2ratio1)/2
manipur_no2ratio2= (manipur2007_no2ratio2+manipur2008_no2ratio2)/2
manipur_no2ratio3= (manipur2007_no2ratio3+manipur2008_no2ratio3)/2

manipur_rspmratio1= (manipur2007_rspmratio1+manipur2008_rspmratio1)/2
manipur_rspmratio2= (manipur2007_rspmratio2+manipur2008_rspmratio2)/2
manipur_rspmratio3= (manipur2007_rspmratio3+manipur2008_rspmratio3)/2

#values of so2 in nagaland,mizoram & assam for every year
assam_SO2=list(air_quality[(air_quality['State']=='Assam')]['so2'])
nagaland_SO2=list(air_quality[(air_quality['State']=='Nagaland')]['so2'])
mizoram_SO2=list(air_quality[(air_quality['State']=='Mizoram')]['so2'])

#finding values of so2 in manipur for every year
manipur_SO2=[]
for i in range(0,10):
    val1=nagaland_SO2[i]*manipur_so2ratio1
    val2=mizoram_SO2[i]*manipur_so2ratio2
    val3=assam_SO2[i]*manipur_so2ratio3
    manipur_SO2.append((val1+val2+val3)/3)

#values of no2 in nagaland,mizoram & assam for every year
assam_NO2=list(air_quality[(air_quality['State']=='Assam')]['no2'])
nagaland_NO2=list(air_quality[(air_quality['State']=='Nagaland')]['no2'])
mizoram_NO2=list(air_quality[(air_quality['State']=='Mizoram')]['no2'])

#finding values of no2 in manipur for every year
manipur_NO2=[]
for i in range(0,10):
    val1=nagaland_NO2[i]*manipur_no2ratio1
    val2=mizoram_NO2[i]*manipur_no2ratio2
    val3=assam_NO2[i]*manipur_no2ratio3
    manipur_NO2.append((val1+val2+val3)/3)

#values of rspm in nagaland,mizoram & assam for every year
assam_rspm=list(air_quality[(air_quality['State']=='Assam')]['rspm'])
nagaland_rspm=list(air_quality[(air_quality['State']=='Nagaland')]['rspm'])
mizoram_rspm=list(air_quality[(air_quality['State']=='Mizoram')]['rspm'])

#finding values of rspm in manipur for every year
manipur_rspm=[]
for i in range(0,10):
    val1=nagaland_rspm[i]*manipur_rspmratio1
    val2=mizoram_rspm[i]*manipur_rspmratio2
    val3=assam_rspm[i]*manipur_rspmratio3
    manipur_rspm.append((val1+val2+val3)/3)

for i in range(0,10):
    if(i!=2 and i!=3):
        missing_rows.append(['Manipur',2005+i,manipur_SO2[i],manipur_NO2[i],manipur_rspm[i]])
        
df=pd.DataFrame(missing_rows,columns=['State','Year','so2','no2','rspm'])
new_air_quality = pd.concat([air_quality, df], ignore_index = True) 
sorted_df = new_air_quality.sort_values(by = ['State', 'Year']) 
sorted_df.reset_index(inplace=True,drop=True)

sorted_df.to_csv('../datasets/Final_Air_Quality_Data.csv',index=False)


# %%



