def twoSum(arr, target):
    s = set()
    for num in arr:
        complement  = target - num
        if complement in s:
            return True
        s.add(num)
    return False

arr = [3,-1,5,-3,7,2]
target = 5
print(twoSum(arr,target))