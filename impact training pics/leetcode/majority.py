def majorityElement(nums):
        size =  len(nums)
        li = []
        no_of_times = size//3
        if no_of_times ==0:
            return list(set(nums))
        my_dict = {}
        for i in nums:
            if i not in my_dict.keys():
                my_dict[i] = 1
            else :
                my_dict[i] += 1
        for key,count in my_dict.items():
            if count > no_of_times:
                li.append(key)
        #del my_dict
        return set(li)
                
                
    
             
nums = [2,2]
res = majorityElement(nums)

print(res)