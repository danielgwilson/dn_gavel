#!/usr/bin/python
# read in.csv adding one column for UUID

import csv
import uuid

fin = open('s_uuid.csv', 'rb')
fout = open('gavel_items.csv', 'w')

reader = csv.reader(fin, delimiter=',', quotechar='"')
writer = csv.writer(fout, delimiter=',', quotechar='"')

for row in reader:
    writer.writerow( (row[2], "https://dn-applications.herokuapp.com/" + row[-1], row[4] + " " + row[7]) )
