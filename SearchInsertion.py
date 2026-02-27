a=[1,2,4,5,6,8,9,10]
n=len(a)
low=0
high=n-1
target=8
lb=n
while low<=high:
    mid=(low+high)//2
    if a[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1
print(lb)

