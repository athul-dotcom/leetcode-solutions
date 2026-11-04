# Pattern: accumulator, track-the-best, digit walker

## 1. Accumulator

Start a variable before the loop, update it each round, use it after the loop.

```python
nums = [4, 8, 15, 16]
total = 0
count_even = 0
for x in nums:
    total += x
    if x % 2 == 0:
        count_even += 1
print(total, count_even)
```

Output:

```text
43 3
```

## 2. Track the best

Keep the best answer so far and update it when something beats it. Start from the first item (or from `-infinity`) so negatives work.

```python
nums = [3, -7, 12, 5]
best = nums[0]
for x in nums:
    if x > best:
        best = x
print(best)
```

Output:

```text
12
```

### Top two (largest and second largest)

When a new number beats `first`, the old `first` becomes `second`.

```python
def top_two(nums):
    first = second = float("-inf")
    for x in nums:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
    return first, second

print(top_two([5, 9, 2, 9, 7]))
```

Output:

```text
(9, 7)
```

## 3. Digit walker

`n % 10` gives the last digit, `n // 10` removes it. Loop until nothing is left.

```python
n = 1234
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)
```

Output:

```text
10
```

Build the reversed number the same way: `rev = rev * 10 + n % 10`.

```python
n = 1200
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)
```

Output:

```text
21
```

## 4. Kadane's idea (best running sum)

Keep the best sum **ending here**. If the running sum goes negative, drop it and start fresh.

```python
def max_subarray(nums):
    current = best = nums[0]
    for x in nums[1:]:
        current = max(x, current + x)
        best = max(best, current)
    return best

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
```

Output:

```text
6
```

## When to reach for these

| Problem says... | Pattern |
|---|---|
| "sum / count of ..." | accumulator |
| "largest / smallest / second largest" | track the best |
| "digits of a number", "reverse a number", "palindrome number" | digit walker |
| "maximum subarray sum" | Kadane |
