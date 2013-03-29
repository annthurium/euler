import sys
matrix = []

def make_matrix(read_file):
	input_file = open(read_file)
	for line in input_file:
		string_line = (line.split())
		new_row = []
		for item in string_line:
			new_item = int(item)
			new_row.append(new_item)
		matrix.append(new_row)
	input_file.close()
	return matrix

def find_greatest_across(greatest, row):
	for i, item in enumerate(row):
		if i > (len(row)-4):
			break
		product = row[i]*row[i+1]*row[i+2]*row[i+3]
		#print "%d * %d * %d * %d = %d." % (row[i], row[i+1], row[i+2], row[i+3], product)
		if product > greatest:
			print "%d * %d * %d * %d = %d." % (row[i], row[i+1], row[i+2], row[i+3], product)
			print "The new greatest is: ", product
			greatest = product
	print row
	print greatest
	return greatest

def main(argv):
	args = sys.argv
	script, read_file = argv
	matrix = make_matrix(read_file)
	greatest = 0
	for row in matrix:
		find_greatest_across(greatest, row)

main(sys.argv)