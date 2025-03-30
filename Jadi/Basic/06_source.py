import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    reader = csv.reader(open(input_file_name))
    writer = csv.writer(open(output_file_name, 'w', newline=''))
    mydict = OrderedDict()

    for i in range(1000, 10000):
        mydict[i] = hashlib.sha256(str(i).encode()).hexdigest()

    mydict = {j: i for i, j in mydict.items()}

    for line in reader:
        name = line[0]
        hash = line[1]

        writer.writerow([name,mydict[hash]])