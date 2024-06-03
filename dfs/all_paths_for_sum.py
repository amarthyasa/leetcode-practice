class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root, target_sum):
    all_paths = []
    has_path(root, target_sum, [], all_paths)
    return all_paths

def has_path(root, target_sum, current_path, all_paths):
    if root is None:
        return False
    current_path.append(root.val)
    if root.val == target_sum and root.left == None and root.right == None:
        all_paths.append(list(current_path))
    
    else:
        has_path(root.left, target_sum - root.val, current_path, all_paths)
        has_path(root.right, target_sum - root.val, current_path, all_paths)
    del current_path[-1]

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree has path: " + str(pathSum(root, 23)))
print("Tree has path: " + str(pathSum(root, 16)))