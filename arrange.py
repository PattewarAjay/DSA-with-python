a=[7,2,-1,-5,6,4,-8]
n=len(a)
res=[0]*n
pos,nev=0,1
for i in range(0,n):
    if a[i]>=0:
        res[pos]=a[i]
        pos+=2
    else:
        res[nev]=a[i]
        nev+=2
print(res)