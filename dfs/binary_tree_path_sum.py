class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path(root, target_sum):
    if root is None:
        return False
    if root.val == target_sum and root.left == None and root.right == None:
        return True
    
    return has_path(root.left, target_sum - root.val) or has_path(root.right, target_sum - root.val)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree has path: " + str(has_path(root, 23)))
print("Tree has path: " + str(has_path(root, 16)))