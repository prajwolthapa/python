import csv

f =open('FL_insurance_sample.csv')
csv_f= csv.reader(f)
v_List=[]
for s in csv_f:
    v_List.append(s)
f.close()

print(v_List)


