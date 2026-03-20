a=[7,2,1,1,3,8,9,10,11,99]
n=len(a)
maxval=0
lowval=float('-inf')
myset=set()
for i in range(n):
    myset.add(a[i])
for num in myset:
    if num-1 not in myset:
        x=num
        count=1
        while x+1 in myset:
            count+=1
            x+=1
        maxval=max(count,maxval)
print(maxval)
    