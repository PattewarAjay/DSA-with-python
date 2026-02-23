a=[1,2,3,-1,-2,-3]
n=len(a)
res=[0]*n
posin,negin=0,1
for i in range(0,n):
    if a[i]>=0:
        res[posin]=a[i]
        posin+=2
    else:
        res[negin]=a[i]
        negin+=2
print(res)