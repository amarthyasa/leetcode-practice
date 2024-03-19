def pair_with_targetsum(arr, target_sum):
    # TODO: Write your code here
    front = 0
    back = len(arr) - 1
    print(front, back)
    while(front < back):
        print(front, back)
        if arr[front] +arr[back] == target_sum:
            return(front, back)
        elif arr[front] +arr[back] > target_sum:
            back-=1
        elif arr[front] +arr[back] < target_sum:
            front+=1

    return None

a = pair_with_targetsum([1, 2, 3, 4, 6], 6)

print(a)

b = pair_with_targetsum([3,2,4], 6)
print(b)