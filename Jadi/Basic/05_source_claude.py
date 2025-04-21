import csv
from statistics import mean

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as input_file, open(output_file_name, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        
        for line in reader:
            name = line[0]
            grades = [float(grade) for grade in line[1:]]
            average = mean(grades)
            writer.writerow([name, average])

def calculate_sorted_averages(input_file_name, output_file_name):
    students = []
    
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        for line in reader:
            name = line[0]
            grades = [float(grade) for grade in line[1:]]
            average = mean(grades)
            students.append((name, average))
    
    # Sort by average, then by name if averages are equal
    students.sort(key=lambda x: (x[1], x[0]))
    
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for name, average in students:
            writer.writerow([name, average])

def calculate_three_best(input_file_name, output_file_name):
    students = []
    
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        for line in reader:
            name = line[0]
            grades = [float(grade) for grade in line[1:]]
            average = mean(grades)
            students.append((name, average))
    
    # Sort by average (descending), then by name if averages are equal
    students.sort(key=lambda x: (-x[1], x[0]))
    
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for name, average in students[:3]:
            writer.writerow([name, average])

def calculate_three_worst(input_file_name, output_file_name):
    students = []
    
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        for line in reader:
            name = line[0]
            grades = [float(grade) for grade in line[1:]]
            average = mean(grades)
            students.append((name, average))
    
    # Sort by average (ascending), then by name if averages are equal
    students.sort(key=lambda x: (x[1], x[0]))
    
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for name, average in students[:3]:
            writer.writerow([average])  # Only writing the average, not name

def calculate_average_of_averages(input_file_name, output_file_name):
    averages = []
    
    with open(input_file_name) as input_file:
        reader = csv.reader(input_file)
        for line in reader:
            grades = [float(grade) for grade in line[1:]]
            average = mean(grades)
            averages.append(average)
    
    overall_average = mean(averages)
    
    with open(output_file_name, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow([overall_average])
