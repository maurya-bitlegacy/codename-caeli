import xlrd
import json
pop_2011={}
wb = xlrd.open_workbook('Table 2.1_4.xls')
sh = wb.sheet_by_name("Table 2.1")

for i in range(8,45):
    cell_value_pop = sh.cell(i,4).value
    cell_value_state = sh.cell(i,0).value
    cell_value_area = sh.cell(i,1).value
    if cell_value_pop=="":
    	continue
    else:
	    if cell_value_state==" A.& N.Islands ":
	    	res=cell_value_state.replace(" A.& N.Islands ","Andaman & Nicobar Islands")
	    elif cell_value_state==" D.& N.Haveli ":
	    	res=cell_value_state.replace(" D.& N.Haveli ","Dadra & Nagar Haveli")
	    # elif cell_value_state==" Puducherry ":
	    # 	res=cell_value_state.replace(" Puducherry ","Pondicherry")
	   
	    elif cell_value_state==" Jammu & Kashmir (1) ++":
	    	res=cell_value_state.replace(" Jammu & Kashmir (1) ++","Jammu & Kashmir")
	    else:
	    	res=cell_value_state.strip()
	    pop_2011[res] = {'Population':cell_value_pop,'Area': cell_value_area}
print(pop_2011)
with open('2011_population.json', 'w') as fp:
    json.dump(pop_2011, fp)

