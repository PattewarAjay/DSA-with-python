a=[1,1,1,1,2,2,3,3,3,4,4,5,5,5]
a.sort()
n=len(a)
myset=set()
target=8
for i in range(0,n):
    if i>0 and a[i]==a[i-1]:
        continue
    for j in range(i+1,n):
        if j>i+1 and a[j]==a[j-1]:
            continue
        k=j+1
        l=n-1
        while k<l:
            sum=a[i]+a[j]+a[k]+a[l]
            if sum<target:
                k+=1
            elif sum>target:
                l-=1
            else:
                temp=[a[i],a[j],a[k],a[l]]
                temp.sort()
                myset.add(tuple(temp))
                k+=1
                l-=1
                while k<l and a[k]==a[k-1]:
                    k+=1  
                while k<l and a[l]==a[l+1]:
                    l-=1
print(myset)