class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_sum_of_path_numbers(root):
    return find_sum(root, 0)

def find_sum(root, total_sum):
    if root is None:
        return 0
    
    total_sum = total_sum*10 + root.val

    if root.left is None and root.right is None:
        return total_sum

    return find_sum(root.left, total_sum) + find_sum(root.right, total_sum)



def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
