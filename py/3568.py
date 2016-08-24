s = input().split()
t = s[0]
for v in list(map(lambda x: x[:-1], s[1:])):
	tt = t
	while v[-1] in ['[', ']', '*', '&']:
		if v[-2:] == '[]':
			tt += v[-2:]
			v = v[:-2]
		else:
			tt += v[-1]
			v = v[:-1]
	print(tt, v + ';')