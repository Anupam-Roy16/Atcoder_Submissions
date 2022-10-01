x,y=map(int,input().split())
v=[[0]*200001]*200001
for i in range(x):
    v1=list(map(int,input().split()))
    v[i]=v1

for i in range(y):
    p,q=map(int,input().split())
    print(v[p-1][q])





















