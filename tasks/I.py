I =  [int(i) for i in input().split()]
Iodd = []
for x in range(len(I)):
    if I[x] % 2 != 0:
        Iodd.append(I[x])
print(f"min odd element ->{min(Iodd)}")