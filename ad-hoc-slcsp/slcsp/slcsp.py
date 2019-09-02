import csv

zips = []
with open('zips.csv') as csvfile:
    reader = csv.reader(csvfile)
    #header
    next(reader)
    for row in reader:
        zips.append((row[0], row[1], row[4]))


plans = []
with open('plans.csv') as csvfile:
    reader = csv.reader(csvfile)
    #header
    next(reader)
    for row in reader:
        if row[2] == 'Silver':
            plans.append((row[1], row[4], row[3]))

slcsp = {}
for z in zips:
    slcsp[z[0]] = []
    for p in plans:
        if (p[0], p[1]) == (z[1], z[2]):
            slcsp[z[0]].append(float(p[2])) 

#    print(list(sorted(dict.fromkeys(slcsp[z[0]]))))
    slcsp[z[0]] = list(sorted(dict.fromkeys(slcsp[z[0]])))
    if len(slcsp[z[0]]) > 1:
        slcsp[z[0]] = slcsp[z[0]][1]
    else:
        slcsp[z[0]] = ''


with open('slcsp.csv', 'w') as csvfile:
    for z in slcsp.keys():
        csvfile.write("%s,%s\n"%(z, slcsp[z]))
