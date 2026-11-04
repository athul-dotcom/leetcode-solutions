# Pattern: prefix and suffix

Precompute running information from the left (prefix) and/or the right (suffix) so each answer needs only O(1) extra work.

## Prefix sums: range sum in O(1)

`prefix[i]` = sum of the first `i` items. Sum of `nums[l:r]` = `prefix[r] - prefix[l]`.

```python
nums = [2, 4, 6, 8]
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
print(prefix)
print(prefix[3] - prefix[1])
```

Output:

```text
[0, 2, 6, 12, 20]
10
```

`prefix[3] - prefix[1]` is the sum of `nums[1:3]` = 4 + 6 = 10.

## Product of array except self (LeetCode 238)

For each position, multiply everything on the left by everything on the right, **without division**.

- Pass 1 (left to right): `result[i]` = product of everything left of `i`.
- Pass 2 (right to left): multiply `result[i]` by the product of everything right of `i`.

```python
def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))
```

Output:

```text
[24, 12, 8, 6]
[0, 0, 9, 0, 0]
```

Time O(n), extra space O(1) beyond the output list.

## When to reach for this

- "sum of a range, many queries" → prefix sums
- "everything except me", "left side vs right side" → prefix + suffix passes
