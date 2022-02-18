s = input()
z = []
y =s.split()
for c in y:
	if int(c) % 2 == 0:
		z.append(int(c))
print(*z)		

