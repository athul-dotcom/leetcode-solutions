# Two pointers: slow and fast (same direction)

`fast` scans every item. `slow` marks the place where the next "good" item should be written. This lets you rearrange an array **in place** in O(n) time and O(1) space.

```text
[ 0, 1, 0, 3, 12 ]
   ^
  slow/fast start together
```

## Move zeros (LeetCode 283)

Push every non-zero to the front, keeping order; zeros end up at the back.

When `fast` finds a non-zero, swap it with `nums[slow]` and advance `slow`.

```python
def move_zeros(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([0, 0, 1]))
print(move_zeros([4, 5]))
```

Output:

```text
[1, 3, 12, 0, 0]
[1, 0, 0]
[4, 5]
```

Idea: everything before `slow` is the finished non-zero part.

## Remove duplicates from a sorted array (LeetCode 26)

Because the array is sorted, duplicates are neighbours. Whenever `fast` sees a new value, write it at `slow + 1`. Return the new length `slow + 1`.

```python
def remove_duplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1

data = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = remove_duplicates(data)
print(k, data[:k])
```

Output:

```text
5 [0, 1, 2, 3, 4]
```

## Sort array by parity (LeetCode 905)

Evens to the front, odds to the back (any order inside each group).

```python
def sort_by_parity(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] % 2 == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

print(sort_by_parity([3, 1, 2, 4]))
```

Output:

```text
[2, 4, 3, 1]
```

This is the same shape as move zeros: "good item" = even instead of non-zero.

## Is subsequence (LeetCode 392)

Is `s` hidden inside `t` in the same order (gaps allowed)? Pointer `i` on `s`, loop over `t`; advance `i` when characters match.

```python
def is_subsequence(s, t):
    i = 0
    for ch in t:
        if i < len(s) and ch == s[i]:
            i += 1
    return i == len(s)

print(is_subsequence("abc", "ahbgdc"), is_subsequence("axc", "ahbgdc"))
```

Output:

```text
True False
```

## Merge sorted array (LeetCode 88): fill from the back

`nums1` has `m` real items followed by `n` empty slots. Fill from the **back** so you never overwrite items you still need.

```python
def merge_arrays(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    return nums1

print(merge_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
```

Output:

```text
[1, 2, 2, 3, 5, 6]
```

## Which two-pointer style?

| Clue in the problem | Style |
|---|---|
| sorted array, pair/target, palindrome, "from both ends" | opposite ends |
| "in place", "keep order", "remove", "move to the end" | slow and fast |
| two sorted sequences to combine | one pointer per sequence |
