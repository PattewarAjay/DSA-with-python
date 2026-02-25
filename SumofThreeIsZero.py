a=[-2,-1,-2,2,3,1,-1,0,0,0]
mylist=[]
a.sort()
n=len(a)
for i in range(0,n):
    if a[i]!=0 and a[i]==a[i-1]:
        continue
    j=i+1
    k=n-1
    while(j<k):
        sum=a[i]+a[j]+a[k]
        if sum<0:
            j+=1
        if sum>0:
            k-=1
        else:
            ans=[a[i],a[j],a[k]]
            mylist.append(ans)
            j+=1
            k-=1
            while j<k and a[j]==a[j-1]:
                j+=1
            while j<k and a[k]==a[k+1]:
                k-=1
print(mylist) 