# Loops and `range`

Loops are how you stop repeating yourself. Almost every DSA problem is a loop with a small idea inside it.

## `range(start, stop, step)`

- `start` is included, `stop` is **not** included.
- `step` defaults to 1. A negative step counts down (then `start` must be bigger than `stop`).

```python
print(*range(1, 6))
print(*range(10, 0, -2))
print(*range(0, 20, 5))
```

Output:

```text
1 2 3 4 5
10 8 6 4 2
0 5 10 15
```

> `print(*something)` unpacks the items and prints them separated by spaces. Handy for output formats.

## `for` loop: when you know how many times

```python
total = 0
for i in range(1, 6):
    total += i
print(total)
```

Output:

```text
15
```

## `while` loop: when you stop on a condition

```python
n = 3
while n > 0:
    print(n)
    n -= 1
```

Output:

```text
3
2
1
```

Always change something inside the loop that moves it towards stopping, otherwise it never ends.

## `break` and `continue`

- `break` leaves the loop completely.
- `continue` skips the rest of this round and goes to the next one.

```python
for i in range(1, 8):
    if i == 3:
        continue
    if i == 6:
        break
    print(i, end=" ")
print()
```

Output:

```text
1 2 4 5
```

## `for ... else`

The `else` runs only if the loop finished **without** hitting `break`.

```python
for x in [1, 3, 5]:
    if x % 2 == 0:
        print("found even")
        break
else:
    print("no even number")
```

Output:

```text
no even number
```

## Nested loops: patterns

Outer loop = rows, inner part = what to print in each row.

```python
for i in range(1, 5):
    print("*" * i)
```

Output:

```text
*
**
***
****
```

```python
for i in range(1, 5):
    print(*range(1, i + 1))
```

Output:

```text
1
1 2
1 2 3
1 2 3 4
```

## Prime check (loop + early return)

You only need to test divisors up to the square root.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print([x for x in range(1, 20) if is_prime(x)])
```

Output:

```text
[2, 3, 5, 7, 11, 13, 17, 19]
```

## Mistakes I made (and fixed)

| Mistake | Why it fails | Fix |
|---|---|---|
| `range(1, -11)` | start is bigger than stop with a positive step, so it is empty | `range(1, -11, -1)` to count down |
| `if x = 5:` | `=` assigns, `==` compares | `if x == 5:` |
| `return` inside a loop that should collect results | it exits on the first round | collect in a list, `return` after the loop |
| `print` instead of `return` in a function | caller gets `None` | `return` the value, print outside |
| Forgetting to update the loop variable in `while` | infinite loop | change it every round |
