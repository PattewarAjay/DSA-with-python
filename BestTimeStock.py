a=[9,2,1,3,4,5,8]
maxn=0
minn=float("inf")
for i in range(0,len(a)):
    if a[i]<minn:
        minn=a[i]
    if a[i]-minn>maxn:
        maxn=a[i]-minn
print(maxn)
