from collections import deque

def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])


    for current_number in nums:
        for _ in range(len(permutations)):
            old_p = permutations.popleft()
            for j in range(len(old_p) + 1):
                new_p = list(old_p)
                new_p.insert(j, current_number)
                if len(new_p) == len(nums):
                    result.append(new_p)
                else:
                    permutations.append(new_p)

    return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()
