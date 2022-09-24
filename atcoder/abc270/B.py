x,y,z=map(int,input().split())
if x>0:
    if y<0 or y>x:
        print(x)
    elif(z>y):
        print("-1")
    elif z>0:
        print(x)
    else:
        z*=-2
        print(z+x)
else:
    if y>0 or y<x:
        print(x*-1)
    elif z<y:
        print("-1")
    elif z<0:
        print(x*-1)
    else:
        z*=2;
        x*=-1
        print(z+x)





