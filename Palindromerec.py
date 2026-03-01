n="mada"
right=len(n)-1
left=0
def pali(n,left,right):
    if left>=right:
        return "palindrome"
    if n[left]!=n[right]:
        return "no"
    return pali(n,left+1,right-1)
print(pali(n,0,len(n)-1))