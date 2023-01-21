n,p,q,r,s=map(int,input().split())
v=list(map(int,input().split()))
v1=[]
t=r-1
p=p-1
q=q-1
r=r-1
s=s-1
for i in range(n):
    if i>=p and i<=q:
        v1.append(v[t])
        t=t+1
    elif i>=r and i<=s:
        v1.append(v[p])
        p=p+1
    else:
        v1.append(v[i])
for i in range(n):
    print(v1[i],end=" ")

