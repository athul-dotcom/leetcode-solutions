# Practice problems: strings

## Caesar shift

Shift each letter by `shift` places, wrapping around the alphabet. The `% 26` does the wrapping. Letters keep their case; other characters stay as they are.

How it works for a lowercase letter `c`:

1. `ord(c) - ord('a')` → position 0..25
2. add `shift`, then `% 26` → wrapped position
3. `+ ord('a')` and `chr(...)` → back to a letter

```python
def caesar(text, shift):
    result = ""
    for c in text:
        if c.islower():
            result += chr((ord(c) - ord("a") + shift) % 26 + ord("a"))
        elif c.isupper():
            result += chr((ord(c) - ord("A") + shift) % 26 + ord("A"))
        else:
            result += c
    return result

print(caesar("Hello, World!", 3))
print(caesar("xyz", 3))
print(caesar(caesar("Hello, World!", 3), -3))
```

Output:

```text
Khoor, Zruog!
abc
Hello, World!
```

Python's `%` always gives a non-negative result for a positive modulus, so negative shifts (decrypting) work too.

## Reverse words in a sentence

`split()` without arguments also removes extra spaces.

```python
def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("the sky is blue"))
print(reverse_words("  hello   world  "))
```

Output:

```text
blue is sky the
world hello
```

## Merge strings alternately (LeetCode 1768)

Take one character from each string in turn; append whatever is left of the longer one.

```python
def merge_alternately(a, b):
    result = []
    i = 0
    while i < len(a) or i < len(b):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])
        i += 1
    return "".join(result)

print(merge_alternately("abc", "pqr"))
print(merge_alternately("ab", "pqrs"))
```

Output:

```text
apbqcr
apbqrs
```

## Count vowels and consonants

```python
def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

print(count_vowels_consonants("Hello World"))
```

Output:

```text
(3, 7)
```

## Same pattern, covered elsewhere

| Problem | Where |
|---|---|
| Palindrome string | `04-two-pointers/01-opposite-ends.md` |
| Valid Palindrome II (LC 680) | `04-two-pointers/01-opposite-ends.md` |
| Is subsequence (LC 392) | `04-two-pointers/02-slow-and-fast.md` |
| Valid anagram, first unique character, reverse vowels, most frequent character | `02-core-patterns/02-frequency-and-hashing.md` |
