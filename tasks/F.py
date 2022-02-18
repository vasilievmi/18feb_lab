s = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(s) - 1):
    if s[i - 1] < s[i] > s[i + 1]:
        counter += 1
print(counter)
