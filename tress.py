class Node:
    def __init__ (self, data):
        self.left = None
        self.right = None
        self.data = data

def print_inorder(root):

    if root:
        print_inorder(root.left)
        print(root.data, " ")
        print_inorder(root.right)

def print_preorder(root):

    if root:
        print(root.data, " ")
        print_preorder(root.left)
        print_preorder(root.right)

def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.data, " ")


def print_levelorder(root):
    queue = []
    res = []
    if root is None:
        return 
    
    queue.append(root)
    while queue:
        level = len(queue)
        curr_level = []
        for _ in range(level):
            curr = queue.pop(0)
            curr_level.append(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(curr_level)
    
    print(res)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
# Function call
print("Inorder traversal of binary tree is")
print_inorder(root)

print("Preorder traversal of binary tree is")
print_preorder(root)

print("levelorder traversal of binary tree is")
print_levelorder(root)