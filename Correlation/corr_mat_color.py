import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

L = []
count = 0

with open("Spearman_corr.csv") as f:
	csvreader = csv.reader(f)
	for line in csvreader:
		count+= 1
		if count==1:
			continue
		temp = []
		for x in line:
			s = ""
			i=1
			while x[i]!=',':
				s+= x[i]
				i+= 1
			temp.append(float(s))
		L.append(temp)
		
label = ['year', 'so2', 'no2', 'rspm', 'industry', 'vehicle', 'pop_den']

fig, ax = plt.subplots()
fig.suptitle('Correlation Matrix', fontsize=16)


min_val, max_val = 0, 7

im = ax.matshow(L, cmap=plt.cm.Oranges)
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.15)

for i in range(7):
    for j in range(7):
        c = L[j][i]
        ax.text(i,j, str(c), va='center', ha='center')
        ax.set_xticklabels(['']+label)
        ax.set_yticklabels(['']+label)

fig.colorbar(im, cax=cax, orientation='vertical')
plt.show()