# fundamental node class for constructing a linkedlist
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

# lets construct a linkedlist 
# A -> B -> C -> D -> None

# define your nodes
# a = Node("A")
# b = Node("B")
# c = Node("C")
# d = Node("D")

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(7)


# construct linkedlists
a.next = b
b.next = c
c.next = d

def print_linked_list(head: Node):
    """
    linkedlist traversal iterative

    Args:
        head (Node): the head node
    """
    current = head
    while current is not None:
        print(current.value)
        current = current.next


def print_linked_list_recursive(head: Node):
    """
    linkedlist traversal recursive

    Args:
        head (Node): the head node
    """
    # we think about our base case
    if head is None:
        return 
    print(head.value)
    print_linked_list_recursive(head.next)


def list_values_iterative(head) -> list:
    """
    Given the head of a linkedlist 
    return the values of the linked in an array


    Args:
        head (Node): head of the linkedlist

    Returns:
        list: returned list
    """
   # result 
    values = []
    # current node 
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values

# for the recursive part of list values
# we need a helper function fillvalues

def fill_values(head, values):
    """
    helper iterative version of linkedlist

    Args:
        head (Node): head node
        values (list): values
    """
    if head is None:
        return 
    
    values.append(head.value)
    fill_values(head.next, values)

def list_values_recursive(head) -> list:
    """
    Given the head of a linkedlist 
    return the values of the linked in an array


    Args:
        head (Node): head of the linkedlist

    Returns:
        list: returned list
    """
    # base case
    values = []
    fill_values(head, values)
    return values

# sum list problem 
def sum_list(head: Node) -> int:
    """
    Given a the head of a linkedlist
    sum the values of all nodes

    time: O(n)
    space: O(1)

    Args:
        head (Node): head node

    Returns:
        int: result: total sum of values in the list
    """
    result = 0
    # set the current node to head
    current = head 

    while current is not None:
        # update result 
        result += current.value
        # reassign current 
        current = current.next
    return result

# to solve the sum list iteratively
# we will need a helper function

def sum_list_iterative(head: Node) -> int:
    """
    Given a the head of a linkedlist
    sum the values of all nodes

    time: O(n)
    space: O(n) # because of the callstack

    Args:
        head (Node): head node

    Returns:
        int: result: total sum of values in the list
    """
    if head is None:
        return 0
    # set the current node to head
    return head.value + sum_list_iterative(head.next)


def list_find_iterative(head: Node, target: any) -> bool:
    """
    Given a the head of a linkedlist and target value
    return True if the target value is in the list 

    time: O(n)
    space: O(1)

    Args:
        head (Node): head node
        target(any): target value

    Returns:
        bool: True if the value exist in the linkedlist
    """
    current = head 

    while current is not None:
        # update result 
        if current.value == target:
            return True
        # reassign current 
        current = current.next
    return False

def list_find_recursive(head: Node, target: any) -> bool:
    """
    Given a the head of a linkedlist and target value
    return True if the target value is in the list 

    time: O(n)
    space: O(n)

    Args:
        head (Node): head node
        target(any): target value

    Returns:
        bool: True if the value exist in the linkedlist
    """
    if head is None:
        return False
    
    if head.value == target:
        return True
    
    return list_find_recursive(head.next, target)

if __name__ == "__main__":
    print(list_find_recursive(a, 2))
    # print(sum_list_iterative(a))
    # print(sum_list(a))
    # print(list_values_recursive(a))
    # print(list_values_iterative(a))
    # print_linked_list_recursive(a)
    # print_linked_list(a)