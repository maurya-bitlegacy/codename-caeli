import csv
import json

with open('2011_population.json') as f:
  data = json.load(f)

area = {}

for x in data:
	for y in data[x]:
		if y == 'Area':
			area[x] = data[x][y]



final = {}

with open("2005_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]] = [line[1]]

with open("2006_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("2007_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("2008_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("2009_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("2010_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("2011_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("2012_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("2013_population.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		final[line[0]].append(line[1])

with open("2014_population.csv") as f:
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


with open('Population_density_final.csv', 'w', newline='') as file:
	wr = csv.writer(file)#,  delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	wr.writerow(['State/UT', 'Year', 'Population_density'])
	for x in res:
		wr.writerow(x)