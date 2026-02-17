a=[2,3,4,5,5,6,7,8,9,10]
n=len(a)
k=3
rotation=k%n
for _ in range(0,k):
    e=a.pop()
    a.insert(0,e)
print(a)