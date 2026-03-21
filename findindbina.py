a=[16,15,14,1,2,3,4,5,6,7,8,9,10]
n=len(a)
l,h=0,n-1
target=4
while l<=h:
    mid=(l+h)//2
    if a[mid]==target:
        print(mid)
    if a[mid]<=a[h]:
        if a[mid]<=target<=a[h]:
            l=mid+1
        else:
            h=mid-1
    else:
        if a[l]<=target<=a[mid]:
            h=mid-1
        else:
            l=mid+1
            print("-1")