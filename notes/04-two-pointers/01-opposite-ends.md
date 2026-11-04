# Two pointers: opposite ends

One pointer at the start (`left`), one at the end (`right`). Move them towards each other until they meet. Works great on **sorted** arrays and on strings.

```text
[ 1, 2, 4, 7, 11, 15 ]
  ^                 ^
 left             right
```

Always initialise both pointers before the loop (`left, right = 0, len(arr) - 1`).

## Pair with a target sum in a sorted array

- sum too small → move `left` right (get a bigger number)
- sum too big → move `right` left (get a smaller number)

```python
def pair_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []

print(pair_sum_sorted([1, 2, 4, 7, 11, 15], 15))
print(pair_sum_sorted([1, 2, 4], 100))
```

Output:

```text
[2, 4]
[]
```

## Palindrome check

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar"), is_palindrome("hello"))
```

Output:

```text
True False
```

## Reverse a list in place

```python
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(reverse_in_place([1, 2, 3, 4, 5]))
```

Output:

```text
[5, 4, 3, 2, 1]
```

## Valid Palindrome II (LeetCode 680)

Can the string become a palindrome after deleting **at most one** character?

Walk inwards. At the first mismatch you must delete either the left or the right character, so check both remaining slices with a helper.

```python
def is_pal(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_pal(s, left + 1, right) or is_pal(s, left, right - 1)
        left += 1
        right -= 1
    return True

print(valid_palindrome("aba"), valid_palindrome("abca"), valid_palindrome("abc"))
```

Output:

```text
True True False
```

**Why is stopping at the first mismatch safe?** Everything outside `left..right` has already matched, so it needs no change. The one allowed deletion must fix the mismatch at `left`/`right`, and the only ways are to remove `s[left]` or `s[right]`. So there are exactly two options to check, and each check is a plain palindrome test.

## Container With Most Water (LeetCode 11)

Two lines form a container; its water is `width * min(height of the two)`. Start with the widest container, then move the **shorter** line inwards.

```python
def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        best = max(best, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))
```

Output:

```text
49
1
```

**Why move the shorter side?** The area is limited by the shorter line. Moving the taller line inwards only makes the width smaller while the height can't exceed the shorter line, so it can never beat the current area. Moving the shorter one is the only move that might find a taller line.

Complexity: O(n) time (each pointer moves at most n times in total), O(1) space.
