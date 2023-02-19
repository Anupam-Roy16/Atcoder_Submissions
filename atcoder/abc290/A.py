x,y=map(int,input().split())
v=list(map(int,input().split()))
v1=list(map(int,input().split()))
p=0
for i in range(y):
    p=p+v[v1[i]-1]
print(p)