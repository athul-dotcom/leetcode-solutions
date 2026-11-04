# Functions

A function packages a piece of logic under a name so you can reuse it and test it.

## Basic shape

```python
def add(a, b):
    return a + b

print(add(2, 3))
```

Output:

```text
5
```

## `return` vs `print`

`print` shows something on the screen. `return` hands a value **back to the caller**. A function with no `return` gives back `None`.

```python
def show(x):
    print(x)

def give(x):
    return x

a = show(5)
b = give(5)
print(a, b)
```

Output:

```text
5
None 5
```

LeetCode checks what you **return**, not what you print.

## Default arguments

```python
def greet(name="friend"):
    return "Hi " + name

print(greet())
print(greet("Athul"))
```

Output:

```text
Hi friend
Hi Athul
```

## Returning more than one value

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([4, 1, 9])
print(lo, hi)
```

Output:

```text
1 9
```

## Helper functions

Break a big problem into small functions. Example: reverse a number using a helper loop and reuse it for a palindrome check.

```python
def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def is_palindrome_number(n):
    return n == reverse_number(n)

print(reverse_number(1234), is_palindrome_number(121), is_palindrome_number(123))
```

Output:

```text
4321 True False
```

## Recursion: a function that calls itself

Needs a **base case** (when to stop) and a **smaller problem** (how it moves towards the base case).

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```text
120
```

## `lambda`: a tiny one-line function

Most useful as a sort key.

```python
words = ["pear", "fig", "banana"]
print(sorted(words, key=lambda w: len(w)))

pairs = [(1, 9), (2, 3), (3, 5)]
print(sorted(pairs, key=lambda p: p[1]))
```

Output:

```text
['fig', 'pear', 'banana']
[(2, 3), (3, 5), (1, 9)]
```

## Variables inside functions

A variable created inside a function exists only there. If you assign to `left` before it has a value (for example you use `left` in a `while` condition without setting `left = 0` first) Python raises `UnboundLocalError`. Always initialise your pointers and counters at the top.
