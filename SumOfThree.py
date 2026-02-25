a=[-1,0,1,2,-1,-4]
n= len(a)
myset=set()
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if a[i]+a[j]+a[k]==0:
                temp=[a[i],a[j],a[k]]
                temp.sort()
                myset.add(tuple(temp))
print([list(app) for app in myset])