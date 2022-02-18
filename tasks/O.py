k = 4
lst = [1,2,3,4,5]
k=k%len(lst)
ret=[0]*len(lst)
for i in range(len(lst)):
    if i+k<len(lst) and i+k>=0:
        ret[i]=lst[i+k]
    if i+k>=len(lst):
        ret[i]=lst[i+k-len(lst)]
    if i+k<0:
        ret[i]=lst[i+k+len(lst)]
print(ret)