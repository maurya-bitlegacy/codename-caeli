import xlrd
# import json
import csv
pop_2011={}
result=[]
wb = xlrd.open_workbook('Table 2.1_4.xls')
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
try:
	with open("2011_population.csv", 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=['State/UT', 'Population','Area'])
		writer.writeheader()
		writer.writerows(result)
except IOError:
    print("I/O error")