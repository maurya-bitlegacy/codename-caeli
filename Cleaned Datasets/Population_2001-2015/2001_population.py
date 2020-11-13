from bs4 import BeautifulSoup
import json
import requests
import csv
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
with open('2001_population.json', 'w') as fp:
    json.dump(dict_population, fp)

try:
	with open("2001_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result)
except IOError:
    print("I/O error")





