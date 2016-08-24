p = []
for i in range(1, 9): p.append((int(input()), i))
p = sorted(p)[-5:]
p0 = sorted([i[0] for i in p])
p1 = sorted([str(i[1]) for i in p])
print(sum(p0))
print(' '.join(p1))