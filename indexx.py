a=[2,3,4,5,5,6,7,8,9,10]
n=len(a)
temp=a[n-1]
for i in range(n-2,-1,-1):
    a[i+1]=a[i]
a[0]=temp
print(a)
