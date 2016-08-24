a,b=map(int,input().split())
if (a+b)%2 or a<b:print(-1)
else:c=sorted([(a+b)//2,abs(a-b)//2]);print(c[1],c[0])