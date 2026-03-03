

n=56773
def nodi(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    return count
print(nodi(n))

