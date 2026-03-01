n=[3,5,1,8,9,4,6]
def sel(n):
    k=len(n)
    for i in range(0,k):
        minn=i
        for j in range(i+1,k):
            if n[j]<n[minn]:
                minn=j
        n[i],n[minn]=n[minn],n[i]
    return n
print(sel(n))