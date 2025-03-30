import csv
from statistics import mean
from collections import OrderedDict 

def calculate_averages(input_file_name, output_file_name):
    reader = csv.reader(open(input_file_name))
    writer = csv.writer(open(output_file_name, 'w', newline=''))

    for line in reader:
        name = line[0]
        grades = list(map(float, line[1:]))
        gpa = str(mean(grades))

        writer.writerow([name,gpa])



def calculate_sorted_averages(input_file_name, output_file_name):
    reader = csv.reader(open(input_file_name))
    writer = csv.writer(open(output_file_name, 'w', newline=''))
    mylist = []

    for line in reader:
        name = line[0]
        grades = list(map(float, line[1:]))
        gpa = mean(grades)
        mylist.append((name, gpa))
    
    mylist.sort()
    mylist.sort(key=lambda x: x[1])

    for i, j in mylist:
        writer.writerow([i,j])
    


def calculate_three_best(input_file_name, output_file_name):
    reader = csv.reader(open(input_file_name))
    writer = csv.writer(open(output_file_name, 'w', newline=''))
    mylist = []

    for line in reader:
        name = line[0]
        grades = list(map(float, line[1:]))
        gpa = mean(grades)
        mylist.append((name, gpa))
    
    mylist.sort()
    mylist.sort(key=lambda x: x[1], reverse=True)

    for i, j in mylist[:3]:
        writer.writerow([i,j])


def calculate_three_worst(input_file_name, output_file_name):
    reader = csv.reader(open(input_file_name))
    writer = csv.writer(open(output_file_name, 'w', newline=''))
    mylist = []

    for line in reader:
        name = line[0]
        grades = list(map(float, line[1:]))
        gpa = mean(grades)
        mylist.append((name, gpa))
    
    mylist.sort()
    mylist.sort(key=lambda x: x[1])

    for i, j in mylist[:3]:
        writer.writerow([j])


def calculate_average_of_averages(input_file_name, output_file_name):
    reader = csv.reader(open(input_file_name))
    writer = csv.writer(open(output_file_name, 'w', newline=''))
    mylist = []

    for line in reader:
        grades = list(map(float, line[1:]))
        gpa = mean(grades)
        mylist.append(gpa)
    
    gpa = mean(mylist)
    writer.writerow(gpa)