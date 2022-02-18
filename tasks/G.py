G =  [int(i) for i in input().split()]
Gmax = max(G)
GmaxIndex = G.index(Gmax)
print(f"Max ->{Gmax}\nPos ->{GmaxIndex+1}")