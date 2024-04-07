def two_sums(nums, target):
    h = {}
    for i, num in enumerate(nums):
        if target - num in h:
            return(h[target - num], i)
        else:
            h[num] = i