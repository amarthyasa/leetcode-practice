class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths(root, S):
    return count_paths_current(root, S, [])

def count_paths_current(current_node, S, current_path):
    if current_node is None:
        return 0

    current_path.append(current_node.val)
    pathCount, pathSum = 0,0
    for i in range(len(current_path) - 1, -1, -1):
        pathSum += current_path[i]
        if pathSum == S:
            pathCount +=1

        
    pathCount += count_paths_current(current_node.left, S, current_path)
    pathCount += count_paths_current(current_node.right, S, current_path)

    del current_path[-1]
    return pathCount
    





def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()
