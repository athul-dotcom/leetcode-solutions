# Pattern: frequency counting and hashing

A dictionary lets you ask "have I seen this?" or "how many times?" in O(1). This is the most common trick in beginner/intermediate problems.

## Frequency counter

```python
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
print(max(freq, key=freq.get))
```

Output:

```text
{'b': 1, 'a': 3, 'n': 2}
a
```

`max(freq, key=freq.get)` returns the key with the biggest value (most frequent character).

## First non-repeating character (two passes)

Pass 1 counts. Pass 2 walks in the original order and returns the first with count 1.

```python
def first_unique(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1

print(first_unique("leetcode"), first_unique("loveleetcode"), first_unique("aabb"))
```

Output:

```text
0 2 -1
```

## Duplicates with a set

```python
nums = [1, 2, 3, 2, 1]
seen = set()
dups = []
for x in nums:
    if x in seen and x not in dups:
        dups.append(x)
    seen.add(x)
print(dups)
```

Output:

```text
[2, 1]
```

## Valid anagram

Two words are anagrams if they have the same letters with the same counts.

```python
def is_anagram(a, b):
    return sorted(a) == sorted(b)

print(is_anagram("listen", "silent"), is_anagram("rat", "car"))
```

Output:

```text
True False
```

## Two Sum

Find two indices whose values add up to `target`.

### Brute force: O(n²)

```python
def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum_brute([2, 7, 11, 15], 9))
```

Output:

```text
[0, 1]
```

### Optimal with a dictionary: O(n) time, O(n) space

For each number, the partner we need is `target - number`. Look in `seen` first, **then** store the current number, so an element is never paired with itself.

```python
def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
```

Output:

```text
[0, 1]
[1, 2]
[0, 1]
```

## Missing number (0..n)

The sum of 0..n is `n*(n+1)//2`. The difference to the actual sum is the missing number.

```python
def missing_number(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

print(missing_number([3, 0, 1]), missing_number([0, 1]))
```

Output:

```text
2 2
```

## Collect, then process

Sometimes you cannot decide in one pass. First collect what you need, then do a second pass. Reverse vowels: collect the vowels, then rebuild the string popping vowels from the end.

```python
def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    found = [c for c in s if c in vowels]
    result = []
    for c in s:
        if c in vowels:
            result.append(found.pop())
        else:
            result.append(c)
    return "".join(result)

print(reverse_vowels("hello"), reverse_vowels("leetcode"))
```

Output:

```text
holle leotcede
```

## When to reach for this

| Problem says... | Tool |
|---|---|
| "how many times", "most frequent" | dict counter |
| "duplicate", "seen before", "unique" | set |
| "find a pair / complement" | dict of value → index |
| "same letters" | counter or `sorted` |
