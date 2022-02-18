M =  [int(i) for i in input().split()]
temp = 0
for x in range(len(M)//2):
    temp = M[len(M)-(x+1)]
    M[len(M)-(x+1)] = M[x]
    M[x] = temp
print(M)