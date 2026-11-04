# Practice problems: arrays

The big ones already have their own notes. This page is the map plus a few extras.

| Problem | Pattern | Where |
|---|---|---|
| Two Sum (LC 1) | dictionary of seen values | `02-core-patterns/02-frequency-and-hashing.md` |
| Missing number (LC 268) | sum formula | `02-core-patterns/02-frequency-and-hashing.md` |
| Product of array except self (LC 238) | prefix + suffix | `02-core-patterns/03-prefix-and-suffix.md` |
| Move zeros (LC 283) | slow and fast | `04-two-pointers/02-slow-and-fast.md` |
| Remove duplicates from sorted array (LC 26) | slow and fast | `04-two-pointers/02-slow-and-fast.md` |
| Merge sorted array (LC 88) | fill from the back | `04-two-pointers/02-slow-and-fast.md` |
| Container With Most Water (LC 11) | opposite ends | `04-two-pointers/01-opposite-ends.md` |
| Maximum sum subarray of size k | fixed window | `05-sliding-window/01-fixed-window.md` |

## Second largest element

```python
def second_largest(nums):
    first = second = float("-inf")
    for x in nums:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    return second

print(second_largest([12, 35, 1, 10, 34, 1]))
```

Output:

```text
34
```

## Rotate a list right by k

Slicing does it in one line. `k % len` handles k bigger than the length.

```python
def rotate_right(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k] if k else nums[:]

print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([1, 2, 3], 4))
```

Output:

```text
[4, 5, 1, 2, 3]
[3, 1, 2]
```

## Contains duplicate (LeetCode 217)

```python
def contains_duplicate(nums):
    return len(set(nums)) != len(nums)

print(contains_duplicate([1, 2, 3, 1]), contains_duplicate([1, 2, 3]))
```

Output:

```text
True False
```

## Single number: the XOR trick (LeetCode 136)

`a ^ a = 0` and `a ^ 0 = a`, so pairs cancel and only the single number remains. O(n) time, O(1) space.

```python
def single_number(nums):
    result = 0
    for x in nums:
        result ^= x
    return result

print(single_number([4, 1, 2, 1, 2]))
```

Output:

```text
4
```
