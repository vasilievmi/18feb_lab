n = input()
m = n.split()
v = int(m[1])
for i in range(len(m)):
	if v < int(m[i]):
		print(int(m[i]), end=' ')
	v = int(m[i])


