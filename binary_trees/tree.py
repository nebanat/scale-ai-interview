"""binary tree module"""
from collections import deque


# node class that represent each node in the tree
# typically a node should have a value, the left and right pointer
class Node:
    def __init__(self, value) -> None:
        self.value =  value
        self.right = None
        self.left = None

# lets construct this below using our node class
#                  a
#               /    \
#              b     c
#           /   \     \
#          d    e      f

# lets define all the nodes 
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")


# lets assign pointers based on the tree above 
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# lets implement our depthfirst traversal iteratively 
# depth first uses a stack to store nodes 
# Space and time complexity O(n)
def depth_first_iteratively(root: Node) -> list:
    """
    depth first iteratively

    Args:
        root (node): root node

    Returns:
        result: a list of tree nodes values traversed depth first
    """
    # edge case of an empty tree
    if root is None:
        return []
    
    result = [] # store node values 
     # initialise our stack with the root node
    stack = [root]
    while len(stack) > 0:
        # we remove from the top of the stack
        current = stack.pop()
        result.append(current.value)

        # we check if the current node has right child
        if current.right is not None:
            stack.append(current.right)
        
         # we check if the current node has left child
        if current.left is not None:
            stack.append(current.left)
    return result


# lets implement the depth first recursively
def depth_first_recursively(root: Node) -> list:
    """
    depth first iteratively

    Args:
        root (node): root node

    Returns:
        result: a list of tree nodes values traversed depth first
    """
    if root is None:
        return []
    # traverse our left subtree
    left_values = depth_first_recursively(root.left) # [b, d, e]
    # traverse our right subtree
    right_values =depth_first_recursively(root.right) # [c, f]

    return [root.value, *left_values, *right_values]


# lets implement our breadth first traversal 
# breadth first uses a queue data structure to store nodes 
# Space complexity O(n)
# time complexity O(n) # given the queue implementation is 0(1)
def breadth_first_iteratively(root: Node) -> list:
    """
    depth first iteratively

    Args:
        root (node): root node

    Returns:
        result: a list of tree nodes values traversed depth first
    """
    # edge case of an empty tree
    if root is None:
        return []
    
    result = [] # store node values 
     
     # initialise our queue with the root node
    queue = deque([root])
    
    while len(queue) > 0:
        # we remove from the top of the queue
        current = queue.popleft() # 0(1)
        # append the value of current node to result list
        result.append(current.value)

        # we check if the current node has left child
        if current.left is not None:
            queue.append(current.left)

        # we check if the current node has right child
        if current.right is not None:
            queue.append(current.right)
        
    return result


if __name__ == '__main__':
    # print(depth_first_iteratively(a))
    # print(depth_first_recursively(a))
    print(breadth_first_iteratively(a))

