# Classes and objects (just enough for linked lists)

A **class** is a blueprint; an **object** is one thing built from it. `__init__` runs when you create an object, and `self` means "this object".

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        return "Pass" if self.marks >= 40 else "Fail"

s = Student("Athul", 72)
print(s.name, s.grade())
```

Output:

```text
Athul Pass
```

## The `Node` class (used all through linked lists)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
print(a.value, a.next.value, b.next)
```

Output:

```text
1 2 None
```

Reading it: `a.next` is node `b`, so `a.next.value` is 2. `b.next` is `None`, which marks the end of the list.

## Things that tripped me up

- `__init__` has **two** underscores on each side and `self` as the first parameter.
- You call `Node(5)`, not `Node.__init__(5)`.
- Compare the value inside a node, not the node itself: `head.value == target`, not `head == target`.
- LeetCode's node class uses `val`, not `value`. Check the field name in the problem.
