n=156
def ams(n):
    num=n
    k=len(str(n))
    result=0
    while num>0:
        rem=num%10
        result+=rem**k
        num=num//10
    return n==result
print(ams(n))