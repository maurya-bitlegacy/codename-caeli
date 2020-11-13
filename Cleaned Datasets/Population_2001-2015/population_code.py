import json
import csv
import math
pop_2002={}
result_2002=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2002[key]=data_2001[key]*(1+rate)
r=sorted(pop_2002.items())
for ele in r:
	result_2002.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2002_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2002)
except IOError:
    print("I/O error")
  
#2003_data
pop_2003={}
result_2003=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2003[key]=data_2001[key]*(1+rate)**2
r=sorted(pop_2003.items())
for ele in r:
	result_2003.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2003_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2003)
except IOError:
    print("I/O error")
#2004_data
pop_2004={}
result_2004=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2004[key]=data_2001[key]*(1+rate)**3
r=sorted(pop_2004.items())
for ele in r:
	result_2004.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2004_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2004)
except IOError:
    print("I/O error")
#2005_data
pop_2005={}
result_2005=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2005[key]=data_2001[key]*(1+rate)**4
r=sorted(pop_2005.items())
for ele in r:
	result_2005.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2005_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2005)
except IOError:
    print("I/O error")

#2006_data
pop_2006={}
result_2006=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

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
	with open("2006_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2006)
except IOError:
    print("I/O error")

#2007_data
pop_2007={}
result_2007=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2007[key]=data_2001[key]*(1+rate)**6
r=sorted(pop_2007.items())
for ele in r:
	result_2007.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2007_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2007)
except IOError:
    print("I/O error")

#2008_data
pop_2008={}
result_2008=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2008[key]=data_2001[key]*(1+rate)**7
r=sorted(pop_2008.items())
for ele in r:
	result_2008.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2008_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2008)
except IOError:
    print("I/O error")

#2009_data    
pop_2009={}
result_2009=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2011=data_2011.keys()

for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2009[key]=data_2001[key]*(1+rate)**8
r=sorted(pop_2009.items())
for ele in r:
	result_2009.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2009_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2009)
except IOError:
    print("I/O error")

#2010_data
pop_2010={}
result_2010=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

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
	with open("2010_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2010)
except IOError:
    print("I/O error")
#2012_data
pop_2012={}
result_2012=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2012[key]=data_2001[key]*(1+rate)**11
r=sorted(pop_2012.items())
for ele in r:
	result_2012.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2012_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2012)
except IOError:
    print("I/O error")

#2013_data
pop_2013={}
result_2013=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2013[key]=data_2001[key]*(1+rate)**12
#print(pop_2013)
r=sorted(pop_2013.items())
for ele in r:
	result_2013.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2013_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2013)
except IOError:
    print("I/O error")

#2014_data
pop_2014={}
result_2014=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2014[key]=data_2001[key]*(1+rate)**13
r=sorted(pop_2014.items())
for ele in r:
	result_2014.append({'State/UT':ele[0],'Population':ele[1]}) 

try:
	with open("2014_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2014)
except IOError:
    print("I/O error")

#2015_data
pop_2015={}
result_2015=[]
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

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
	with open("2015_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population'])
		writer.writeheader()
		writer.writerows(result_2015)
except IOError:
    print("I/O error")