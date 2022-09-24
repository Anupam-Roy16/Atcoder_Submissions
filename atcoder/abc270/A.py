p,q=map(int,input().split())
v=[0]*3
if(p==1):
    v[0]+=1
elif(p==3):
    v[0]+=1
    v[1]+=1
elif(p==5):
    v[0] += 1
    v[2] += 1
elif(p==2):
    v[1] += 1
elif(p==4):
    v[2] += 1
elif(p==6):
    v[2] += 1
    v[1] += 1
elif(p==7):
    v[0] += 1
    v[1] += 1
    v[2]+=1

if(q==1):
    v[0]+=1
elif(q==3):
    v[0]+=1
    v[1]+=1
elif(q==5):
    v[0] += 1
    v[2] += 1
elif(q==2):
    v[1] += 1
elif(q==4):
    v[2] += 1
elif(q==6):
    v[2] += 1
    v[1] += 1
elif(q==7):
    v[0] += 1
    v[1] += 1
    v[2]+=1
e=7
for j in range(3):
    if v[j]==0:
        if j==0:
            e-=1
        elif j==1:
            e-=2
        elif j==2:
            e-=4
print(e)


