w = []
k = []
for i in range(10): w.append(int(input()))
for i in range(10): k.append(int(input()))
w = sorted(w)
k = sorted(k)
print(sum(w[-3:]), sum(k[-3:]))