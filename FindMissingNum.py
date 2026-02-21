n=[9,8,6,4,1,2,3,0,7]

def fin(n):
    sum=0
    d=len(n)
    for i in range(0,d):
        sum+=n[i]
    return (d*(d+1))/2 - sum
print(fin(n))