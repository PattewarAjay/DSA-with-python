a=[2,3,4,5,5,6,7,8,10]
target=13
def fin(a,target):
    has={}
    for i in range(0,len(a)):
        if target-a[i] not in has:
            has[a[i]]=i
        else:
            return has[target-a[i]],i
print(fin(a,target) )
