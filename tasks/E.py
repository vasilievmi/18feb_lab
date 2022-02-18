E =  [int(i) for i in input().split()]
resStrPos = ""
resStrNeg = ""
for x in range(len(E)):
    if E[x] < 0:
        resStrPos += str(E[x])
    else:
        resStrNeg += str(E[x])
    if len(resStrPos) > 2 | len(resStrNeg) >2:
        break
if len(resStrPos) < len(resStrNeg):
    print(resStrNeg)
else: 
    print(resStrPos)