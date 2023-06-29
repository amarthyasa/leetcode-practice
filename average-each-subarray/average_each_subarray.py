'''
find the average of each subarray containing k elements


Solution:

sliding window
'''

def average_subarray(arr, K):
    result = []
    w_sum, w_start = 0.0, 0
    for w_end in range(len(arr)):
        w_sum += arr[w_end]
        if w_end >= K-1:
            result.append(w_sum/K)
            w_sum -= arr[w_start]
            w_start +=1
    return(result)
    




A = [3,-4,2,7,8,10]
x = average_subarray(A, 5)
print(x)