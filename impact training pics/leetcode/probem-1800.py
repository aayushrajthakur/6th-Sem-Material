def maximumSubArray(nums):
    stack = []
    size = len(nums)
    if size == 0:
        return 0
    res = 0
    max_sum = 0
    for i in range(size-1):
        current = nums[i]
        res = nums[i]
        if nums[i] <= nums[i+1]:
            res  += nums[i]
        else:
            stack.append(max(res, nums[i]))
            res = 0
    return stack

nums = [3,2,5,7,1,5,9]
print(maximumSubArray(nums))