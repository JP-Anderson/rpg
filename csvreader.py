#csv reader

import csv
from exampleClass import ExampleClass

with open('example.csv', 'rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',', quotechar="|")
	
	data = []
	
	for row in csvreader:
		data.append(row)

dataRows = len(data)

print "dataRows = " + str(dataRows)

fieldHeaders = data[0]

exampleClasses = []

for i in range (1,dataRows):
	print "We're on iteration " + str(i)
	exampleClasses.append(ExampleClass())
	
	print "We now have " + str(len(exampleClasses)) + " items in our class array!"
	
	exampleClasses[i-1].field1 = int(data[i][0])
	exampleClasses[i-1].field2 = data[i][1]
	exampleClasses[i-1].field3 = int(data[i][2])
	exampleClasses[i-1].field4 = float(data[i][3])
	
def minus(x,y):
	return x-y

x = exampleClasses[1].field3
y = exampleClasses[2].field3

print minus(x,y)
print minus(y,x)