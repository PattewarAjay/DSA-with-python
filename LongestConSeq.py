a=[99,100,4,200,1,3,2]
n=len(a)
maxcount=0
for i in range(0,n):
    key=a[i]
    count=1
    while key+1 in a:
        count+=1
        key +=1
    maxcount=max(count,maxcount)
print(maxcount)