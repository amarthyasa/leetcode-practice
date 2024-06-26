from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    ltr = True
    while queue:
        level_size = len(queue)
        current_level = deque()
        for i in range(level_size):
            current_node = queue.popleft()
            if ltr:
                current_level.append(current_node.val)
                ltr = False
            else:
                current_level.appendleft(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        result.append(current_level) 
    return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("zigzag order traversal: " + str(traverse(root)))


main()
