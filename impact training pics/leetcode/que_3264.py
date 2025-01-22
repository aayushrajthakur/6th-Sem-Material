
def getFinalState(nums, k, multiplier):
    for i in range(k):
        index = nums.index(min(nums))
        minimum = min(nums)
        minimum *= multiplier
        nums[index] = minimum
    print(nums)
        

li = [2,1,3,5,6]
k = 5
mul = 2
getFinalState(li,k,mul)