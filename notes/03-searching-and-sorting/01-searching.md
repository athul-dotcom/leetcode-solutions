# Searching

## Linear search: O(n)

Check every item. Works on anything, sorted or not.

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([4, 2, 9, 7], 9), linear_search([4, 2, 9, 7], 5))
```

Output:

```text
2 -1
```

## Binary search: O(log n), needs a **sorted** array

Look at the middle. If the target is bigger, throw away the left half; if smaller, throw away the right half. Each step halves the search space.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7), binary_search([1, 3, 5, 7, 9, 11], 4))
```

Output:

```text
3 -1
```

### `left <= right` vs `left < right`

- `while left <= right` : the window `[left, right]` can hold one last candidate. Use it when you **return the index of an exact match**.
- `while left < right` : you are narrowing down to a single answer position (like "first bad version"), and `right = mid` keeps the candidate.

### Search insert position (LeetCode 35)

If the target is missing, `left` ends up exactly where it should be inserted.

```python
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

data = [1, 3, 5, 6]
print(search_insert(data, 5), search_insert(data, 2), search_insert(data, 7), search_insert(data, 0))
```

Output:

```text
2 1 4 0
```

### First bad version (LeetCode 278)

Versions go good, good, ..., bad, bad. Find the first bad one. `is_bad` is given by the judge; here a lambda stands in for it.

```python
def first_bad_version(n, is_bad):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if is_bad(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(first_bad_version(10, lambda v: v >= 4))
```

Output:

```text
4
```

If `mid` is bad it **might be the first**, so keep it (`right = mid`). If `mid` is good, the answer is after it (`left = mid + 1`).

### Search in rotated sorted array (LeetCode 33)

One half of the window is always sorted. Find which half, check if the target lies in it, and discard the other half.

```python
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0), search_rotated([4, 5, 6, 7, 0, 1, 2], 3))
```

Output:

```text
4 -1
```

## Quick comparison

| Search | Needs sorted? | Time | Space |
|---|---|---|---|
| Linear | no | O(n) | O(1) |
| Binary | yes | O(log n) | O(1) |
