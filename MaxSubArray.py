a=[-2,1,-3,4,-1,2,1,-5,4]
def maxsub(a):
    n=len(a)
    sum=0
    maxs=0
    for i in range(0,n):
        sum+=a[i]
        maxs=max(sum,maxs)
        if sum<0:
            sum=0
    return maxs
print(maxsub(a))
    