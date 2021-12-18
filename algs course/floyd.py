def main():
	reader = open("floyd.in", 'r')

	n = int(reader.readline())
	d = []
	for _ in range(n):
		d.append([int(x) for x in reader.readline().split()])
	for i in range(n):
		for j in range(n):
			for k in range(n):
				if d[j][k] > d[j][i] + d[i][k]:
					d[j][k] = d[i][k] + d[j][i]

	writer = open("floyd.out", 'w')

	for i in range(n):
		writer.write(" ".join(list(map(str, d[i]))) + "\n")
main()