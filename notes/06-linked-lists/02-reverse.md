# Linked lists: reverse (LeetCode 206)

Reversing means flipping every arrow so each node points to the node **before** it.

```text
before:  1 -> 2 -> 3 -> None
after:   3 -> 2 -> 1 -> None
```

## Three pointers

- `prev` : the already-reversed part (starts as `None`, not `head`!)
- `current` : the node being flipped
- `next_node` : saved before flipping, otherwise you lose the rest of the list

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

def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

head = build([1, 2, 3, 4])
print_list(head)
head = reverse_list(head)
print_list(head)
```

Output:

```text
1 -> 2 -> 3 -> 4 -> None
4 -> 3 -> 2 -> 1 -> None
```

## The four lines in the loop, in this order

1. `next_node = current.next` : remember the rest
2. `current.next = prev` : flip the arrow
3. `prev = current` : the reversed part grows by one
4. `current = next_node` : move on

At the end `current` is `None` and `prev` is the new head, so `return prev`.

## Trace for `1 -> 2 -> 3`

| step | current | prev (after) | list built so far |
|---|---|---|---|
| start | 1 | None | |
| 1 | 1 → 2 | 1 | 1 -> None |
| 2 | 2 → 3 | 2 | 2 -> 1 -> None |
| 3 | 3 → None | 3 | 3 -> 2 -> 1 -> None |

## Edge cases

```python
print_list(reverse_list(build([])))
print_list(reverse_list(build([7])))
```

Output:

```text
 -> None
7 -> None
```

Time O(n), space O(1).

## Mistakes I made

- Setting `prev = head` at the start. That makes the old head point to itself and creates a loop. `prev` starts as `None`.
- Changing `current.next` before saving `next_node`.
- Returning `head` instead of `prev`.
