import json
import csv
import math
pop_2002={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2002[key]=data_2001[key]*(1+rate)
#print(pop_2002)
with open('2002_population.json', 'w') as fp:
    json.dump(pop_2002,fp)

    
#2003_data
pop_2003={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2003[key]=data_2001[key]*(1+rate)**2
#print(pop_2003)
with open('2003_population.json', 'w') as fp:
    json.dump(pop_2003,fp)

#2004_data
pop_2004={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2004[key]=data_2001[key]*(1+rate)**3
#print(pop_2004)
with open('2004_population.json', 'w') as fp:
    json.dump(pop_2004,fp)

#2005_data
pop_2005={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2005[key]=data_2001[key]*(1+rate)**4
#print(pop_2005)
with open('2005_population.json', 'w') as fp:
    json.dump(pop_2005,fp)

#2006_data
pop_2006={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2006[key]=data_2001[key]*(1+rate)**5
#print(pop_2006)
with open('2006_population.json', 'w') as fp:
    json.dump(pop_2006,fp)

#2007_data
pop_2007={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2007[key]=data_2001[key]*(1+rate)**6
#print(pop_2007)
with open('2007_population.json', 'w') as fp:
    json.dump(pop_2007,fp)

#2008_data
pop_2008={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2008[key]=data_2001[key]*(1+rate)**7
#print(pop_2008)
with open('2008_population.json', 'w') as fp:
    json.dump(pop_2008,fp)

#2009_data    
pop_2009={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

# pop_keys_2001=data_2001.keys()
pop_keys_2011=data_2011.keys()

for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2009[key]=data_2001[key]*(1+rate)**8
#print(pop_2009)
with open('2009_population.json', 'w') as fp:
    json.dump(pop_2009,fp)

#2010_data
pop_2010={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2010[key]=data_2001[key]*(1+rate)**9
#print(pop_2010)
with open('2010_population.json', 'w') as fp:
    json.dump(pop_2010,fp)

#2012_data
pop_2012={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2012[key]=data_2001[key]*(1+rate)**11
#print(pop_2012)
with open('2012_population.json', 'w') as fp:
    json.dump(pop_2012,fp)

#2013_data
pop_2013={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2013[key]=data_2001[key]*(1+rate)**12
#print(pop_2013)
with open('2013_population.json', 'w') as fp:
    json.dump(pop_2013,fp)


#2014_data
pop_2014={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2014[key]=data_2001[key]*(1+rate)**13
#print(pop_2014)
with open('2014_population.json', 'w') as fp:
    json.dump(pop_2014,fp)

#2015_data
pop_2015={}
with open('2001_population.json') as json_file:
    data_2001 = json.load(json_file)

with open('2011_population.json') as json_file:
    data_2011 = json.load(json_file)

pop_keys_2001=data_2001.keys()
# print(pop_keys_2001)
pop_keys_2011=data_2011.keys()
# print(pop_keys_2001)
# rate=10**(-0.1*math.log(data_2011[key]/data_2001[key])
for key in pop_keys_2011:
	l=(0.1*math.log10(data_2011[key]["Population"]/(data_2001[key])))
	# print(l)
	rate=pow(10,l)-1
	# print(rate)

	pop_2015[key]=data_2001[key]*(1+rate)**14
#print(pop_2015)

with open('2015_population.json', 'w') as fp:
    json.dump(pop_2015,fp)
