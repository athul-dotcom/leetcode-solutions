# Sliding window: variable size

The window grows with `right` and **shrinks from the left with a `while` loop** whenever it breaks the rule. The answer is the best window seen.

Template:

```text
left = 0
for right in range(len(data)):
    add data[right] to the window
    while window breaks the rule:
        remove data[left] from the window
        left += 1
    update the best answer using right - left + 1
```

Use `while` (not `if`) for shrinking, because you may need to drop several items.

## Longest subarray with sum ≤ limit (positive numbers)

```python
def longest_with_sum_at_most(nums, limit):
    left = 0
    current_sum = 0
    best = 0
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum > limit:
            current_sum -= nums[left]
            left += 1
        best = max(best, right - left + 1)
    return best

print(longest_with_sum_at_most([1, 2, 3, 4, 5, 1, 1], 10))
```

Output:

```text
4
```

The longest block is `[1, 2, 3, 4]` with sum 10. This only works when all numbers are positive (so removing from the left always lowers the sum).

## Longest substring without repeating characters (LeetCode 3)

The window must contain **unique** characters. A `set` remembers what is inside. If the new character is already in the set, shrink from the left until it isn't.

```python
def length_of_longest_substring(s):
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best

for word in ["abcabcbb", "bbbbb", "pwwkew", ""]:
    print(repr(word), length_of_longest_substring(word))
```

Output:

```text
'abcabcbb' 3
'bbbbb' 1
'pwwkew' 3
'' 0
```

Time O(n): `left` and `right` each move forward at most n times.

## Minimum size subarray with sum ≥ target (LeetCode 209, practice next)

Here the rule is reversed: shrink while the window is **big enough**, recording the smallest length each time.

```python
def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    best = float("inf")
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            best = min(best, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return 0 if best == float("inf") else best

print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]), min_subarray_len(100, [1, 2, 3]))
```

Output:

```text
2 0
```

## Fixed vs variable at a glance

| | Fixed | Variable |
|---|---|---|
| Window size | always k | grows and shrinks |
| Shrink | automatically (one in, one out) | `while` loop on a rule |
| Keywords | "of size k" | "longest", "shortest", "at most", "without repeating" |
