class TreeNode:
    def __init__(self,val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    return check_sequence(root, sequence, 0)

def check_sequence(current_node, sequence, sequenceIndex):
    if current_node is None:
        return False

    sequence_len = len(sequence)

    if sequenceIndex >= sequence_len or current_node.val != sequence[sequenceIndex]:
        return False

    if current_node.left is None and current_node.right is None and sequenceIndex == sequence_len - 1:
        return True

    return check_sequence(current_node.left, sequence, sequenceIndex + 1) or check_sequence(current_node.right, sequence, sequenceIndex + 1)




def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()