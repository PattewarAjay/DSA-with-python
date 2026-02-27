a=[1,2,3,4,5,6,7,8,9,10]
target=8
def bs(a,target):
    n=len(a)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==target:
            return mid
        elif a[mid]<target:
            low=mid+1
        elif a[mid]>target:
            high=mid-1
    return -1
print(bs(a,target))