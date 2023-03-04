x,y=map(int,input().split())
l=[0]*(x+1)
for i in range(y):
    p,q = map(int, input().split())
    if p==3:
        if l[q]==-1:
            print("Yes")
        else:
            print("No")
    elif p==2:
        l[q]=-1
    else:
        if l[q]==0:
            l[q]=1
        else:
            l[q]=-1



