# Linked lists on LeetCode, and what to practise next

## LeetCode's node uses `val`, not `value`

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

On LeetCode the class is already written in a comment at the top. You only write the function, and the input is the `head`. To test on your own machine you need helpers:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

print(to_list(reverse_list(from_list([1, 2, 3, 4, 5]))))
```

Output:

```text
[5, 4, 3, 2, 1]
```

The **dummy node** trick (`dummy = ListNode()`, build after it, return `dummy.next`) removes the special case for an empty/first node. It will be useful below.

---

# Next up (not practised yet)

These are the standard linked-list questions to do next. Code is here so you can read it, then close it and rebuild it from memory.

## Middle of the list (LeetCode 876): slow and fast

`fast` moves two steps, `slow` one. When `fast` reaches the end, `slow` is in the middle.

```python
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

print(middle(from_list([1, 2, 3, 4, 5])).val)
print(middle(from_list([1, 2, 3, 4])).val)
```

Output:

```text
3
3
```

For an even length it returns the second of the two middle nodes.

## Cycle detection (LeetCode 141): Floyd's tortoise and hare

If there is a loop, the fast pointer eventually laps the slow one and they meet.

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

a = from_list([1, 2, 3, 4])
print(has_cycle(a))

b = from_list([1, 2, 3, 4])
tail = b
while tail.next:
    tail = tail.next
tail.next = b.next
print(has_cycle(b))
```

Output:

```text
False
True
```

Use `is` (same object), not `==` (same value).

## Merge two sorted lists (LeetCode 21): dummy node + two pointers

```python
def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

merged = merge_two_lists(from_list([1, 2, 4]), from_list([1, 3, 4]))
print(to_list(merged))
```

Output:

```text
[1, 1, 2, 3, 4, 4]
```

## Checklist

- [ ] Middle of the list
- [ ] Cycle detection
- [ ] Merge two sorted lists
- [ ] Remove nth node from end (two pointers with a gap of n)
- [ ] Palindrome linked list (middle + reverse second half)
