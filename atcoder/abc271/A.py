n=int(input())
v=[]
while 1:
    p=n%16
    if p==10:
        v.append("A")
    elif p==11:
        v.append("B")
    elif p==12:
        v.append("C")
    elif p==13:
        v.append("D")
    elif p==14:
        v.append("E")
    elif p==15:
        v.append("F")
    else:
        v.append(p)
    n=n/16
    n=int(n)
    if n==0:
        break
if len(v)==1:
    print("0",end="")
    print(v[0])
else:
    print(v[1], end="")
    print(v[0])



















