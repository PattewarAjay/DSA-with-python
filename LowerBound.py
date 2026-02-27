a=[1,1,1,2,3,3,3,4,5,6,7,8,9,10]
n=len(a)
low=0
high=n-1
target=9
ub=n
while low<=high:
    mid=(low+high)//2
    if a[mid]>target:
        ub=mid
        high=mid-1
    else:
        low=mid+1
print(ub)

