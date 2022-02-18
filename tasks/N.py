n, m = [int(i) for i in input().split()], []
if len(n) % 2 == 0:
    for i in range(len(n)):
	    if i % 2 != 0:
		    m.append(n[i])
		    m.append(n[i-1])
elif len(n) % 2 != 0:
    for i in range(len(n)):
	    if i % 2 != 0:
		    m.append(n[i])
		    m.append(n[i-1])
    m.append(n[-1])		 		
print(*m)



