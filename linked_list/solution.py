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

def get_node_value_iterative(head: Node, index: int) -> any:
    """
    Given the an index value
    get the node value of a linkedlist at index

    time: O(n)
    space: O(1)


    Args:
        head (Node): head node
        index (int): target 
    """
    counter = 0
    current = head

    while current is not None:
        if counter == index:
            return current.value
        
        counter += 1
        current = current.next

    return None

def get_node_value_recursive(head: Node, index: int) -> any:
    """
    Given the an index value
    get the node value of a linkedlist at index

    time: O(n)
    space: O(1)


    Args:
        head (Node): head node
        index (int): target 
    """
    if head is None:
        return None
    
    if index == 0:
        return head.value
    
    return get_node_value_iterative(head.next, index - 1)


def reverse_list_iterative(head: Node) -> Node:
    """
    reverse a linked list

    time: O(n)
    space: O(1)


    Args:
        head (Node): head node
        index (int): target 
    """
    prev = None
    current = head

    while current is not None:
        # step 1
        next = current.next
        current.next = prev
        # step 2
        prev = current
        current = next
    
    return prev
    
def reverse_list_recursive(head: Node, prev = None) -> Node:
    """
    reverse a linked list

    time: O(n)
    space: O(1)


    Args:
        head (Node): head node
        index (int): target 
    """
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list_recursive(next, head)


def zipped_list(head1: Node, head2: Node) -> Node:
    """
    Given two heads of linkedlists for e.g

    A -> B -> C -> D

    E -> F -> G

    you suppose to zip 

    A -> E -> B -> F -> C -> G -> D

    current1 & current2 & tail & count 

    if the count is even we pick from list2 and append to the tail 

    first iteration:

    tail = head1
    current1 = head1.next
    current2 = head2

    Args:
        head1 (Node): head node for list1
        head2 (Node): head node for list2
    """
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 is not None and current2 is not None:
        if count % 2 == 0:
            # pick from the second list
            tail.next = current1
            current1 = current1.next
        else:
            # pick from the first list 
            tail.next = current2
            current2 = current2.next
        
        # progress our tail
        tail = tail.next
        count += 1
    
    # for uneven number of list 
    # if current1 still have node tail.next should point to it 
    if current1 is not None: tail.next = current1
    # if current2 still have node tail.next should point to it 
    if current2 is not None: tail.next = current2

    return head1




if __name__ == "__main__":
    print(get_node_value_recursive(a, 3))
    # print(get_node_value_iterative(a, 4))


    