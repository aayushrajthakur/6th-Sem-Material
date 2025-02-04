def maximumSubArray(nums):
    size = len(nums)
    if size == 0:
        return 
    stack = []
    res = 0
    for i in range(size-1):
        if nums[i] < nums[i+1]:
            res  += nums[i]
        else:
            stack.append(res)
            res = 0
    return stack
    
nums = [3,2,5,7,1,5,9]
print(maximumSubArray(nums))