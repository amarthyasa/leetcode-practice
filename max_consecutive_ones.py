def max_consecutive_ones(nums, k):
    k_local = 0
    max_ones = 0
    start = 0

    for i in range(0, len(nums)):

        if nums[i] == 0:
            k_local +=1

        
        
        while k_local > k:
            if nums[start] == 0:
                k_local -= 1
                
            start += 1
        
        max_ones = max(max_ones, i-start + 1)

    return(max_ones)

print(max_consecutive_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))