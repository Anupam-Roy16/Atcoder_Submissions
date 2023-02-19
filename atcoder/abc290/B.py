x,y=map(int,input().split())
s=input()
s=list(s)
p=0
for i in range(x):
    if p<y and s[i]=='o':
        p=p+1
    elif s[i]=='o':
        s[i]='x'
s=''.join(s)
print(s)