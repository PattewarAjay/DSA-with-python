n=[2,3,6,7,4,7,2,9]
right=len(n)-1
left=0
def rever(n,left,right):
    if left>=right:
        return
    n[left],n[right]=n[right],n[left]
    rever(n,left+1,right-1)
    return n
print(rever(n,0,len(n)-1))