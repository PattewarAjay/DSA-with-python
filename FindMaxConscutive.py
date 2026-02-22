nums=[1,1,0,1,0,1,1,1,1]
def maxcon(a):
    count=0
    maxcount=0
    for i in range(0,len(nums)):
        if nums[i] == 1:
            count+=1
        else:
            maxcount=max(maxcount,count)
            count=0
    return max(maxcount,count)
print(maxcon(nums))