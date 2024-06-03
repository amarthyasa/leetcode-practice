class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def display(root):
    temp = root
    while temp != None:
        print(temp.data)
        temp = temp.next
    if temp is None:
        print("noNE")

def remove_node_from_end(root, n):
    n = n
    slow_pointer = root
    fast_pointer = root
    if not root:
        return None
    else:
        while(n>0):
            fast_pointer = fast_pointer.next
            n = n-1
        if not fast_pointer:
            return root.next
        print("fp data", fast_pointer.data)
        while(fast_pointer.next != None):
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        # print("fp data 2", fast_pointer.data)
        # print("sp data", slow_pointer.data)
        if slow_pointer.next:
            slow_pointer.next = slow_pointer.next.next 
        else:
            slow_pointer.next = None

        return root


        

       

   


root = Node(1)
# root.next = Node(2)
# root.next.next = Node(3)
# root.next.next.next = Node(4)
# root.next.next.next.next = Node(5)
display(root)
remove_node_from_end(root, 1)
print("ans")
display(root)