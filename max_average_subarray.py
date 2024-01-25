"""
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

def findMaxAverage(nums, k):
    sum = 0
    avg = 0
    for i in range(0,k):
        sum = sum +nums[i]
    avg = sum/k
    for i in range(k, len(nums)):
        sum = sum - nums[i-k]
        sum = sum + nums[i]
        t_avg = sum/k
        if t_avg > avg:
            avg = t_avg



    return avg

print(findMaxAverage([1,12,-5,-6,50,3], 4))
    