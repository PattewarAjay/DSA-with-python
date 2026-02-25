a=[1,0,-1,0,-2,2]
n=len(a)
ans=[]
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if a[i]+a[j]+a[k]+a[l]==0:
                    temp=[a[i],a[j],a[k],a[l]]
                    temp.sort()
                    ans.append(temp)
print(ans)