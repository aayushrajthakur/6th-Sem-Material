def permute( nums): 
    def backtrack(start):
        if start == len(nums):
            if (nums[:] not in li):
                li.append(nums[:])
            return
        for i in range(start,len(nums)):
            nums[start],nums[i] = nums[i],nums[start]
            backtrack(start+1)
            nums[start],nums[i] = nums[i],nums[start]
    li = []
    backtrack(0)
    return li


li = [1,1,3]
print(permute(li))