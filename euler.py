import sys

def make_matrix(read_file):
	with open(read_file) as input_file:
		return [[int(i) for i in line.split()] for line in input_file]

def products(matrix, length):
	for i, row in enumerate(matrix):
		for j, item in enumerate(row):
			yield reduce(lambda x, y: x * y, row[j:j+length])
			try:
				yield reduce(lambda x, y: x * y, [matrix[i + offset][j] for offset in range(length)])
				yield reduce(lambda x, y: x * y, [matrix[i + offset][j + offset] for offset in range(length)])
			except IndexError:
				pass
			try:
				yield reduce(lambda x, y: x * y, [matrix[i + offset][j - offset] for offset in range(length)])
			except IndexError:
				pass

def main(argv):
	args = sys.argv
	script, read_file = argv
	length = 4
	print max(products(make_matrix(read_file), length))

main(sys.argv)