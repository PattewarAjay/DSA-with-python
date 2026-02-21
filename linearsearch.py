nums=[2,3,0,9,5,0,4,0,0,1]
n=len(nums)
target=5
for i in range(0,n):
    if nums[i]==target:
        return i
return -1