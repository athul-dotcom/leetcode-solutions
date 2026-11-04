# Linked lists: delete a node by value

To delete a node you rewire the node **before** it so it skips over the target: `previous.next = previous.next.next`. So the walk must **stop on the node before the target**.

Two cases:

1. The target is the head: the new head is `head.next`.
2. The target is somewhere later: stop at the node before it and skip it.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def build(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def print_list(head):
    parts = []
    current = head
    while current is not None:
        parts.append(str(current.value))
        current = current.next
    print(" -> ".join(parts) + " -> None")

def delete_value(head, target):
    if head is None:
        return None
    if head.value == target:
        return head.next
    current = head
    while current.next is not None and current.next.value != target:
        current = current.next
    if current.next is not None:
        current.next = current.next.next
    return head

print_list(delete_value(build([10, 20, 30]), 20))
print_list(delete_value(build([10, 20, 30]), 10))
print_list(delete_value(build([10, 20, 30]), 30))
print_list(delete_value(build([10, 20, 30]), 99))
```

Output:

```text
10 -> 30 -> None
20 -> 30 -> None
10 -> 20 -> None
10 -> 20 -> 30 -> None
```

## Reading the `while` condition

`current.next is not None and current.next.value != target`

- First part: don't fall off the end of the list.
- Second part: stop as soon as the **next** node is the target.
- The order matters. If you reversed them, `current.next.value` would crash when `current.next` is `None`.

## Mistakes I made

- `head == target`: compares a node to a number. It must be `head.value == target`.
- Walking until `current.value == target`: now you are standing **on** the target and cannot rewire the node before it.
- Forgetting the "target is the head" case.

## Delete a node when you only have that node (LeetCode 237)

You cannot reach the previous node, so copy the next node's value into this one and skip the next node.

```python
def delete_given_node(node):
    node.value = node.next.value
    node.next = node.next.next

h = build([4, 5, 1, 9])
delete_given_node(h.next)
print_list(h)
```

Output:

```text
4 -> 1 -> 9 -> None
```
