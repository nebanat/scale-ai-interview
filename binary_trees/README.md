### Binary Tree

A tree structure that has :
- At most 2 children 
- Exactly one root node
- Exactly one path between the root node and any other node
  
      
            ┌───┐
            │ 1 │
            └───┘
            /     \
        ┌───┐     ┌───┐
        │ 2 │     │ 3 │
        └───┘     └───┘


### Traversal 
- **Depth first**:
  - **Time complexity**: O(n) *# of nodes*
  - **Space complexity**: O(n) *# of nodes*
  - **Characteristics**:
    - *Solved both iteratively and recursively*
    - *Uses a stack data structure for traversal when solving iteratively*
- - **Breadth first**:
  - **Time complexity**: O(n) *# of nodes*; Given that queue implementation is O(1)
  - **Space complexity**: O(n) *# of nodes*
  - **Characteristics**:
    - *Uses a queue data structure for traversal when solving iteratively*


### Supporting Materials
- [pop vs pop(0)](https://stackoverflow.com/questions/34633178/why-is-the-big-o-of-pop-different-from-pop0-in-python)
- [Efficient queue implementation](https://stackoverflow.com/questions/45688871/implementing-an-efficient-queue-in-python)
- [Deque](https://docs.python.org/3/library/collections.html#deque-objects)