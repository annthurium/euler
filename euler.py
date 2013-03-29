from sys import argv
script, read_file = argv

matrix = []

#MAX_SIZE = 20

with open(read_file) as input_file:
	for i, line in enumerate(input_file):
		newline = (line.split())
		#for items in newline:

		matrix.append(newline)

for items in matrix[0]:git i
	print "type,", type(items)
