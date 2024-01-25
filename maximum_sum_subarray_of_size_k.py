def max_sub_array_of_size_k(k, arr):
  f_sum = 0
  sum = 0
  for i in range(0,k):
    sum = sum + arr[i]

  f_sum = sum
  for i in range(k, len(arr)):
    sum = sum - arr[i-k]
    sum = sum + arr[i]  
    print(sum)
    if sum> f_sum:
      f_sum = sum
  return f_sum

print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))