n=1228
def nodi(n):
    num=n
    res=0
    while n>0:
        rem=n%10
        res=res*10+rem
        n=n//10
    return num==res
print(nodi(n))