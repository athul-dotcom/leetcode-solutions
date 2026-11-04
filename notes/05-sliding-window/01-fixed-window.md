# Sliding window: fixed size

A window is a block of `k` neighbouring items. Instead of recomputing the sum for every block (O(n·k)), **slide** it: add the new item entering on the right, subtract the item leaving on the left.

```text
[2, 1, 5, 1, 3, 2]   k = 3

[2, 1, 5] 1  3  2     sum = 8
 2 [1, 5, 1] 3  2     sum = 8 - 2 + 1 = 7
 2  1 [5, 1, 3] 2     sum = 7 - 1 + 3 = 9   <- best
 2  1  5 [1, 3, 2]    sum = 9 - 5 + 2 = 6
```

## Maximum sum of a subarray of size k

```python
def max_sum_k(nums, k):
    current = sum(nums[:k])
    best = current
    for i in range(k, len(nums)):
        current += nums[i] - nums[i - k]
        best = max(best, current)
    return best

print(max_sum_k([2, 1, 5, 1, 3, 2], 3))
print(max_sum_k([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3))
```

Output:

```text
9
16
```

- `nums[i]` is the item entering the window.
- `nums[i - k]` is the item leaving the window.

Time O(n), space O(1).

## Maximum average of a subarray of size k (LeetCode 643)

Same idea, divide by `k` at the end.

```python
def max_average(nums, k):
    current = sum(nums[:k])
    best = current
    for i in range(k, len(nums)):
        current += nums[i] - nums[i - k]
        best = max(best, current)
    return best / k

print(max_average([1, 12, -5, -6, 50, 3], 4))
```

Output:

```text
12.75
```

## Move zeros as a "window"

The "non-zero finished part" in move zeros (see two-pointers) behaves like a window that only grows. Same code, shown here because it keeps coming up with sliding-window sets.

```python
def move_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

print(move_zeros([0, 1, 0, 3, 12]))
```

Output:

```text
[1, 3, 12, 0, 0]
```

## Recognising a fixed window

- "subarray / substring of size k"
- "every block of k consecutive items"
- "average / sum / maximum of k items"
