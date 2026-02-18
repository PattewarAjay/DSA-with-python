a=[2,3,4,5,5,6,7,8,9,10]
def reverse(a,left,right):
    while left<right:
        a[left],a[right]=a[right],a[left]
        left+=1
        right-=1
n=len(a)
k=3
reverse(a,n-k,n-1)
reverse(a,0,n-k-1)
reverse(a,0,n-1)
print(a)