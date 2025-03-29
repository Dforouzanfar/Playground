import csv
from statistics import mean
from collections import OrderedDict 

def calculate_averages(input_file_name, output_file_name):
    reader = csv.reader(open(input_file_name))
    writer = csv.writer(open(output_file_name, 'w', newline=''))
    mydict = OrderedDict()

    for line in reader:
        name = line[0]
        grades = list(map(float, line[1:]))
        gpa = mean(grades)
        mydict[name] = str(gpa)

        writer.writerow(f"{name},str(gpa)")



def calculate_sorted_averages(input_file_name, output_file_name):
    


def calculate_three_best(input_file_name, output_file_name):
    


def calculate_three_worst(input_file_name, output_file_name):
    


def calculate_average_of_averages(input_file_name, output_file_name):
    