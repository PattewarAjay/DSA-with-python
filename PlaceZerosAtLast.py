nums=[2,3,0,9,5,0,4,0,0,1]
n=len(nums)
temp=[]
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])
nz=len(temp)
for i in range(0,nz):
    nums[i]=temp[i]
for i in range(nz,n):
    nums[i]=0
print(nums)

nums=[2,3,0,9,5,0,4,0,0,1]
n=len(nums)
i=0
while i<n:
    if nums[i]==0:
        break
    i +=1
if i==n:
    print(nums)
j=i+1
while j<n:
        if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        j+=1
print(nums)