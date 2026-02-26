a=[1,2,3,4,5,6,7,8,9,10]
n=len(a)
target=8
low=0
high=n-1
def binsea(a,low,high):   
    mid=(low+high)//2
    if low>high:
        return -1
    if a[mid]==target:
        return mid
    elif a[mid]<target:
        return binsea(a,mid+1,high)
    elif a[mid]>target:
        return binsea(a,low,mid-1)
   
print(binsea(a,low,high))
        