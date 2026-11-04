# Lists, strings, dictionaries, sets

## Lists (ordered, changeable)

```python
nums = [3, 1, 2]
nums.append(4)
nums.insert(0, 9)
print(nums)
nums.sort()
print(nums)
print(nums.pop(), nums)
print(len(nums), sum(nums), max(nums), min(nums))
```

Output:

```text
[9, 3, 1, 2, 4]
[1, 2, 3, 4, 9]
9 [1, 2, 3, 4]
4 10 4 1
```

Swap two items without a temp variable:

```python
a = [10, 20, 30]
a[0], a[2] = a[2], a[0]
print(a)
```

Output:

```text
[30, 20, 10]
```

List comprehension: build a list in one line.

```python
squares = [x * x for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]
print(squares, evens)
```

Output:

```text
[1, 4, 9, 16, 25] [0, 2, 4, 6, 8]
```

## Slicing: `s[start:stop:step]`

`stop` is **not** included. Works on lists and strings.

```python
s = "abcdef"
print(s[1:4])
print(s[:3])
print(s[-2:])
print(s[::-1])
print(s[::2])
```

Output:

```text
bcd
abc
ef
fedcba
ace
```

Useful for LeetCode: `s[left:right+1]` is the substring from `left` to `right` **inclusive**. A copy of a list is `nums[:]`.

## Strings (ordered, **not** changeable)

You cannot do `s[0] = "x"`. Build a new string or work with a list of characters.

```python
s = "  Hello World  "
print(s.strip())
print(s.lower(), s.upper().strip())
print("a,b,c".split(","))
print("-".join(["x", "y", "z"]))
print("abc123".isalnum(), "123".isdigit(), "abc".isalpha())
print(ord("a"), chr(98))
```

Output:

```text
Hello World
  hello world   HELLO WORLD
['a', 'b', 'c']
x-y-z
True True True
97 b
```

## Dictionaries (key → value, very fast lookup)

```python
d = {"a": 1}
d["b"] = 2
print(d.get("c", 0))
print("a" in d)
for key, value in d.items():
    print(key, value)
```

Output:

```text
0
True
a 1
b 2
```

`d.get(key, default)` never crashes on a missing key. This one idea powers the frequency counter pattern.

## Sets (unique items, very fast `in`)

```python
seen = set()
for x in [1, 2, 2, 3, 3, 3]:
    seen.add(x)
print(seen, 2 in seen, 9 in seen)
print(len(set([1, 2, 2, 3])))
```

Output:

```text
{1, 2, 3} True False
3
```

## Speed cheat-sheet

| Operation | list | set / dict |
|---|---|---|
| `x in container` | O(n) | O(1) |
| append | O(1) | O(1) |
| insert at front | O(n) | n/a |

If a loop does `if x in some_list` inside another loop, swap that list for a set or dict and the whole thing drops from O(n²) to O(n).
