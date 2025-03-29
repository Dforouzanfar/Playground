import csv
from statistics import mean
from collections import OrderedDict 

reader = csv.reader(open("/workspaces/Playground/Jadi/Basic/05_data.csv"))
writer = csv.writer(open("/workspaces/Playground/Jadi/Basic/05_Task1.csv", 'w', newline=''))
mydict = OrderedDict()

for line in reader:
    name = line[0]
    grades = list(map(float, line[1:]))
    gpa = mean(grades)

    writer.writerow(f"{name},str(gpa)")