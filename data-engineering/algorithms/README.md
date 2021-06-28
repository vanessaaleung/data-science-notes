# Algorithms Foundation

<p align="center">
  <img src="https://www.agorapulse.com/social-media-lab/wp-content/uploads/sites/6/2020/06/instagram-algorithm-image.png" height="300px">
</p>

- [Measuring Algorithm Performance](#measuring-algorithm-performance)
- [Common Data Structures](#common-data-structures)
- [Recursion](#recursion)
- [Sorting Data](#sorting-data)
- [Searching Data](#searching-data)
- [Other Algorithms](#other-algorithms)

## Measuring Algorithm Performance
- Big-O notation: classifies performance as the input size grows
  - "O": the order of operation: time scale to perform an operation
- Common Big-O Terms

|Notation  |Description  |Example                                                 |
|----------|-------------|--------------------------------------------------------|
|O(1)      |Constant time|Looking up a single element in an array                 |
|O(log n)  |Logarithmic  |Finding an item in a sorted array with a binary search  |
|O(n)      |Linear time  |Searching an unsorted array for a specific value        |
|O(n log n)|Log-linear   |Complex sorting algorithms like heap sort and merge sort|
|O(n^2)    |Quadratic    |Simple sorting algorithm, such as bubble sort, selection sort, and insertion sort|


## Common Data Structures
- [Arrays](#arrays)
- [Linked Lists](#linked-lists)
- [Stacks and Queues](#stacks-and-queues)
- [Hash Tables](#hash-tables)

### Arrays
_Collection of elements identified by index or key_
- Insert/Delete at beginning/in middle: O(n), since the remaining items have to be moved
- Insert/Delete at the end: O(1)

### Linked Lists
_Collection of nodes_
- Contain reference to the next node in the list
- Easier and faster to iterate sequentially
- Elements can be easily inserted and removed
- Underlying memory doesn't need to be reorganized like arrays
- Can't do constant-time random item access
- Item lookup: O(n)

```python
# the Node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        # TODO: find the first item with a given value
        item = self.head
        while item != None:
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return
        if idx == 0:
            self.head = self.head.next
        else:
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# create a linked list and insert some items
itemlist = LinkedList()
itemlist.insert(38)
itemlist.insert(49)
itemlist.insert(13)
itemlist.insert(15)
itemlist.dump_list()

# Node:  15
# Node:  13
# Node:  49
# Node:  38
# Item count:  4

# exercise the list
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(13))
print("Finding item: ", itemlist.find(78))

# delete an item
itemlist.deleteAt(3)
print("Item count: ", itemlist.get_count())
print("Finding item: ", itemlist.find(38))
itemlist.dump_list()
# Item count:  3
# Finding item:  None
# Node:  15
# Node:  13
# Node:  49
```

### Stacks and Queues
- Stack
  - LIFO: the last item pushed is the first one popped
  - Application: math expression processing, backtracking like browser back stack
- Queue
  - FIFO: first added is the first item out
  - Application: order processing, messaging (make sure msgs are sent in order)

- Stack
```python
# TODO: create a new empty stack
stack = []

# TODO: push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

# TODO: print the stack contents
print(stack) # [1, 2, 3, 4]

# TODO: pop an item off the stack
x = stack.pop()
print(x)     # 4
print(stack) # [1, 2, 3]
```

- Queue
```python
from collections import deque

# TODO: create a new empty deque object that will function as a queue
queue = deque()

# TODO: add some items to the queue
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# TODO: print the queue contents
print(queue)   # deque([1, 2, 3, 4])

# TODO: pop an item off the front of the queue
x = queue.popleft()
print(x)      # 1
print(queue)  # deque([2, 3, 4])
```

### Hash Tables
- i.e. Dictionary
- Maps keys to associated values using the hash function
- Hash function: Uses the key to compute an index into a slot, map the key to the value. Assign each key to a unique slot in the table
- Benefits: very fast, key-to-value mappings are unique
- Drawback: when entries are small, array might be more efficient as there won't be collision to solve. Doesn't order entries in a predictable way


## Recursion

## Sorting Data

## Searching Data

## Other Algorithms
