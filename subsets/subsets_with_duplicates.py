def find_subsets(nums):
    list.sort(nums)
    subsets = []
    subsets.append([])
    s_index, e_index = 0, 0
    for i in range(len(nums)):
        s_index = 0
        if i>0 and nums[i] == nums[i-1]:
            s_index = e_index + 1
        e_index = len(subsets) - 1
        for j in range(s_index, e_index + 1):
            temp = list(subsets[j])
            temp.append(nums[i])
            subsets.append(temp)

    
    return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
