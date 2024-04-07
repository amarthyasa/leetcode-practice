def remove_duplicates(nums):
    next_non_dplicate = 1
    i = 0
    while(i < len(nums)):
        if nums[i] != nums[next_non_dplicate - 1]:
            nums[next_non_dplicate] = nums[i]
            next_non_dplicate+=1
        
        i = i+1
    
    return next_non_dplicate

print(remove_duplicates([1,1,2]))



