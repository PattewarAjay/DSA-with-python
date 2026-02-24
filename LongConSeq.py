a=[1,2,3,4,100,200,1,2,1]
n=len(a)
maxcount=0
myset=set()
for i in range(0,n):
    myset.add(a[i])
for num in a:
    if num-1 not in myset:
        n=num
        count=1
        while n+1 in myset:
            count+=1
            n+=1
        maxcount=max(maxcount,count)
print(maxcount)
