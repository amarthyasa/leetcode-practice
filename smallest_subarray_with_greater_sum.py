def smallest_subarray_with_greater_sum(arr, S):
    front = 0
    back = 0
    sum = 0
    l = S+1
    for i in range(0, len(arr)):
        sum = sum + arr[i]
        back+=1
        while sum >= S:
            temp = back - front 
            if temp < l:
                l = temp
            sum = sum - arr[front]
            front+=1
    return l
            




a = smallest_subarray_with_greater_sum([2, 1, 5, 2, 8], S=7)
print(a)