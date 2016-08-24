r=1
for i in range(int(input())):
    r*=i+10
    r//=i+1
print(r%10007)