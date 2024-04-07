def two_sum(nums, target_sum, triplets):
    # print(nums, target_sum, triplets)
    left = 0
    right = len(nums) - 1
    while(left < right):
        # print('left, right: ', left, right)
        if (nums[right] + nums[left]) == target_sum:
            triplets.append([-target_sum, nums[left], nums[right]])
            left +=1
            right -=1
        elif ((nums[right] + nums[left]) < target_sum):
            left+=1
        else:
            right-=1
    return triplets




def three_sum(nums):
    nums.sort()
    triplets=[]
    for i in range(0, len(nums)):
        if ((nums[i] == nums[i-1]) and i>0):
            continue
        two_sum(nums[i:], -nums[i], triplets)
    return triplets

print(three_sum([-1,0,1,2,-1,-4]))
print(three_sum([0,0,0,0]))