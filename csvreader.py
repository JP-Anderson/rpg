#csv reader

import csv
from exampleClass import ExampleClass

class CsvReader:

	def read(csvfile):
		with open(csvfile, 'rt') as csvfile:
			csvreader = csv.reader(csvfile, delimiter=',', quotechar="|")
			
			data = []
			
			for row in csvreader:
				data.append(row)
			
			return data
