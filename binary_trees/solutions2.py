from collections import deque


# node class that represent each node in the tree
# typically a node should have a value, the left and right pointer
class Node:
    def __init__(self, value) -> None:
        self.value =  value
        self.right = None
        self.left = None


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


def max_depth_tree(root):
    """
    Given a binary tree, calculate the max depth of the tree

                3  |1
            /      \
           |2 9       20 |2
                /      \
                15      7
    """
    if root is None:
        return 0
    
    left_depth = max_depth_tree(root.left)
    right_depth = max_depth_tree(root.right)
    
    return max(left_depth, right_depth) + 1




if __name__ == "__main__":
    print(max_depth_tree(a))

