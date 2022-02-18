C =  [int(i) for i in input().split()]
temp = 0
for x in range(len(C)):
    if C[x] > 0:
        temp+=1
print(temp)