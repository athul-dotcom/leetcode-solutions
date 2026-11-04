# IBM / online-assessment style problems

Typical shape: read the input yourself, solve, print exactly the expected output. See `01-python-foundations/04-input-handling.md` for the input patterns.

## Email validation with a regex

```python
import re

pattern = r"^[A-Za-z0-9._$-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$"

for email in ["athul@gmail.com", "a.b$c@site-1.org", "bad@@x.com", "no_at.com", "x@y.c"]:
    print(email, bool(re.match(pattern, email)))
```

Output:

```text
athul@gmail.com True
a.b$c@site-1.org True
bad@@x.com False
no_at.com False
x@y.c False
```

Reading the pattern piece by piece:

| Piece | Meaning |
|---|---|
| `^` ... `$` | match the whole string, start to end |
| `[A-Za-z0-9._$-]+` | one or more allowed characters before the `@` (inside `[]`, `.` and `$` are literal; put `-` last) |
| `@` | a literal at-sign |
| `[A-Za-z0-9-]+` | domain name |
| `\.` | a literal dot (a bare `.` means "any character") |
| `[A-Za-z]{2,}` | ending of at least 2 letters (`com`, `org`, `in`) |

Quantifiers: `+` = one or more, `*` = zero or more, `?` = zero or one, `{2,}` = two or more.

## Full program with input: sum of a list and its maximum

```python
# stdin: 5|3 9 2 7 4
n = int(input())
nums = list(map(int, input().split()))
print(sum(nums))
print(max(nums))
```

Output:

```text
25
9
```

## Full program with input: Caesar cipher

```python
# stdin: Hello, World!|3
text = input()
shift = int(input())
out = ""
for c in text:
    if c.islower():
        out += chr((ord(c) - ord("a") + shift) % 26 + ord("a"))
    elif c.isupper():
        out += chr((ord(c) - ord("A") + shift) % 26 + ord("A"))
    else:
        out += c
print(out)
```

Output:

```text
Khoor, Zruog!
```

## Full program with input: Fibonacci triangle

```python
# stdin: 4
n = int(input())
fib = [0, 1]
while len(fib) < n:
    fib.append(fib[-1] + fib[-2])
for i in range(1, n + 1):
    print(*fib[:i])
```

Output:

```text
0
0 1
0 1 1
0 1 1 2
```

## Full program with input: find the missing element

Given `n` and `n-1` distinct numbers from 1..n, print the missing one.

```python
# stdin: 5|1 2 4 5
n = int(input())
nums = list(map(int, input().split()))
print(n * (n + 1) // 2 - sum(nums))
```

Output:

```text
3
```

## Test-day checklist

- Read the input format twice. Count lines and spaces.
- Write the logic as a function, test it on the sample, then wire up `input()`.
- Think of edge cases: empty input, one element, all equal, negatives, zero.
- Match the output format exactly; remove debug prints.
- If a loop is nested, ask: can a `set` or `dict` remove one level?
