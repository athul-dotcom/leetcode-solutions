# Linked lists: node, build, traverse, insert

A linked list is a chain of nodes. Each node holds a `value` and a pointer `next` to the following node. The last node's `next` is `None`. We only keep the `head` (the first node).

```text
head
 |
[10 | •]--->[20 | •]--->[30 | None]
```

Lists have O(1) insert at the front but O(n) to reach the i-th item (you must walk from the head).

## The node

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

## Traverse and print

Walk with a `current` pointer until it becomes `None`.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    parts = []
    current = head
    while current is not None:
        parts.append(str(current.value))
        current = current.next
    print(" -> ".join(parts) + " -> None")

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
print_list(head)
```

Output:

```text
10 -> 20 -> 30 -> None
```

## Insert at the beginning: O(1)

New node points at the old head, and becomes the new head. **Return the new head.**

```python
def insert_at_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node

head = insert_at_beginning(head, 5)
print_list(head)
```

Output:

```text
5 -> 10 -> 20 -> 30 -> None
```

## Insert at the end: O(n)

Two cases: the list is empty (the new node is the head), or walk to the last node (`current.next is None`) and attach.

```python
def insert_at_end(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

head = insert_at_end(head, 40)
print_list(head)

empty = insert_at_end(None, 1)
print_list(empty)
```

Output:

```text
5 -> 10 -> 20 -> 30 -> 40 -> None
1 -> None
```

## Build a list from a Python list

```python
def build(values):
    head = None
    for v in values:
        head = insert_at_end(head, v)
    return head

print_list(build([1, 2, 3, 4]))
print_list(build([]))
```

Output:

```text
1 -> 2 -> 3 -> 4 -> None
 -> None
```

(An empty list prints just `-> None`; that's fine for testing.)

## Count and search

```python
def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

def contains(head, target):
    current = head
    while current is not None:
        if current.value == target:
            return True
        current = current.next
    return False

h = build([7, 8, 9])
print(length(h), contains(h, 8), contains(h, 5))
```

Output:

```text
3 True False
```

## Two loop conditions to remember

| Condition | Stops at | Use when |
|---|---|---|
| `while current is not None` | after the last node | you need to visit every node |
| `while current.next is not None` | **on** the last node | you need to change the last node's `next` |
