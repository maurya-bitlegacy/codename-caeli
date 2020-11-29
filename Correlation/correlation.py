import matplotlib.pyplot as plt
from scipy.stats import pearsonr 
from scipy.stats import spearmanr
import numpy as np
import csv

d = {}
count = 0

with open("Final_Air_Quality_Data.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		count+= 1
		if count==1:
			continue
		d[line[0],line[1]] = [line[2], line[3], line[4]]


with open("Cleaned Datasets/Industries-UpdatedFormat.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		if (line[0],line[1]) in d:
			d[line[0],line[1]].append(line[2])


with open("Cleaned Datasets/MotorVehicles-UpdatedFormat.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		if (line[0],line[1]) in d:
			d[line[0],line[1]].append(line[2])

with open("Cleaned Datasets/Population_2001-2015/Population_density_final.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		if (line[0],line[1]) in d:
			d[line[0],line[1]].append(line[2])


label = ['year', 'so2', 'no2', 'rspm', 'industry', 'vehicle', 'pop_den']

inp = []

for x in d:
	if len(d[x]) != 6:  # one or more features missing
		continue
	elif len(d[x]) == 6:
		f = 0
		for y in d[x]:
			if y=='':
				f = 1
				break
		if f == 1:
			continue

	temp = []
	temp.append(x[1])
	for i in d[x]:
		temp.append(i)
	inp.append(temp)


year = []
so2 = []
no2 = []
rspm = []
industry = []
vehicle = []
pop_den = []

for x in inp:
	year.append(x[0])
	so2.append(x[1])
	no2.append(x[2])
	rspm.append(x[3])
	industry.append(x[4])
	vehicle.append(x[5])
	pop_den.append(x[6])


year = [float(i) for i in year]
so2 = [float(i) for i in so2]
no2 = [float(i) for i in no2]
rspm = [float(i) for i in rspm]
industry = [float(i) for i in industry]
vehicle = [float(i) for i in vehicle]
pop_den = [float(i) for i in pop_den]

corr_inp = [year, so2, no2, rspm, industry, vehicle, pop_den]


#print(len(year), len(so2), len(no2), len(rspm), len(industry), len(vehicle), len(pop_den))


corr_res_p = []
corr_res_s = []



for i in range (len(corr_inp)):
	temp_p = []
	temp_s = []
	for j in range (len(corr_inp)):
		x = corr_inp[i]
		y = corr_inp[j]

		corr, p = pearsonr(x,y)
		corr, p = round(corr,4), round(p,4)
		temp_p.append([corr,p])

		corr, p = spearmanr(x,y)
		corr, p = round(corr,4), round(p,4)
		temp_s.append([corr,p])


	corr_res_p.append(temp_p)
	corr_res_s.append(temp_s)


#Pearson
with open('Pearson_corr.csv', 'w', newline='') as file:
	wr = csv.writer(file)#,  delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	wr.writerow(label)
	for x in corr_res_p:
		wr.writerow(x)

#Spearman
with open('Spearman_corr.csv', 'w', newline='') as file:
	wr = csv.writer(file)#,  delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	wr.writerow(label)
	for x in corr_res_s:
		wr.writerow(x)
	
#Scatter plots

fig = plt.figure(0)
fig.suptitle('Scatter plots of features', fontsize=16)
for i in range(7):
    for j in range(7):
        ax = plt.subplot2grid((7,7), (i,j))
        ax.scatter(corr_inp[j], corr_inp[i])
        if j==0:
        	ax.set_ylabel(label[i])
        if i==6:
        	ax.set_xlabel(label[j])
        	if j==0:
        		ax.set_xticks([2005,2010])
        if j!=0 and i!=6:
        	'''
        	x_axis = ax.axes.get_xaxis()
        	x_axis.set_visible(False)

        	y_axis = ax.axes.get_yaxis()
        	y_axis.set_visible(False)
        	'''

        	ax.axes.xaxis.set_ticklabels([])
        	ax.axes.yaxis.set_ticklabels([])

        if j==0 and i!=6:
        	#x_axis = ax.axes.get_xaxis()
        	#x_axis.set_visible(False)
        	ax.axes.xaxis.set_ticklabels([])

        if i==6 and j!=0:
        	#y_axis = ax.axes.get_yaxis()
        	#y_axis.set_visible(False)
        	ax.axes.yaxis.set_ticklabels([])

        

plt.show()


