"""binary tree module"""
from collections import deque
from math import inf

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
# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# numerical nodes
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

# lets assign pointers based on the tree above 
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def tree_includes_iteratively(root: Node, target: str) -> bool:
    """
    Iterative version

    Given the root node of binary tree and target 

    return True if target is contained in the tree
           else return False

    Args:
        root (Node): root node
        target (str): target value

    Returns:
        bool: True or False
    """
    if root is None:
        return False
    
    queue = deque([root])

    while len(queue) > 0:
        cur_node = queue.popleft()
        # check if current node value is equal to target
        if cur_node.value == target:
            return True
        
        # add left child to the queue if it exists 
        if cur_node.left is not None: queue.append(cur_node.left)
        # add right child to the queue if it exists
        if cur_node.right is not None: queue.append(cur_node.right)

    return False


def tree_includes_recursive(root: Node, target: str) -> bool:
    """
    recursive version

    Given the root node of binary tree and target 

    return True if target is contained in the tree
           else return False

    Args:
        root (Node): root node
        target (str): target value

    Returns:
        bool: True or False
    """
    # base case for empty tree
    if root is None:
        return False
    
    # base case for if root == target
    if root.value == target:
        return True
    
    # logical OR (left subtree, right subtree)
    return tree_includes_recursive(root.left, target) or tree_includes_recursive(root.right, target)

def tree_sum(root: Node) -> int:
    """
    tree sum 

    Args:
        root (Node): node

    """
    if root is None: return 0

    return root.value + tree_sum(root.left) + tree_sum(root.right)

def tree_min_value_iterative(root: Node) -> int:
    """
    given the root of a binary tree
    find the smallest number on the tree

    Args:
        root (Node): node

    """
    # check if empty treee
    # if root is None:
    #     return None
    # lets assign a variable for min value
    min_value = +inf
    # queue to hold tree values
    queue = deque([root])

    while len(queue) > 0:
        cur_node = queue.popleft()
        if cur_node.value < min_value:
            min_value = cur_node.value
        
        # left node
        if cur_node.left is not None:
            queue.append(cur_node.left)
        
        # right node 
        if cur_node.right is not None:
            queue.append(cur_node.right)
    
    return min_value


def tree_min_value_recursive(root: Node) -> int:
    """
    given the root of a binary tree
    find the smallest number on the tree

    Args:
        root (Node): node

    """
    if root is None:
        return inf
    
    # min value of the left subtree
    left_min = tree_min_value_recursive(root.left)
    # min value of the right subtree
    right_min = tree_min_value_recursive(root.right)

    return min(root.value, left_min, right_min )
        

def tree_max_path_recursive(root: Node) -> int:
    """
    given the root of a binary tree
    find the maximum root to leaf sum path within the tree

    Args:
        root (Node): node

    """
    if root is None:
        return -inf
    
    if root.left is None and root.right is None:
        return root.value
   
     # min value of the left subtree
    left_max_child = tree_max_path_recursive(root.left)
    # min value of the right subtree
    right_max_child = tree_max_path_recursive(root.right)

    return root.value + max(left_max_child, right_max_child)


if __name__ == "__main__":
    print(tree_max_path_recursive(a))
    # print(tree_min_value_recursive(a))
    # print(tree_min_value_iterative(a))
    # print(tree_sum(a))
    # print(tree_includes_recursive(a, "c"))
    # print(tree_includes_iteratively(a, "c"))
