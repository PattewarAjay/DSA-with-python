n=56773
while n>0:
    res=n%10
    n=n//10
    print(res)

---------------------

n=56773
def nodi(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
print(nodi(n))

---------------------