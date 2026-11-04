# Input handling (online tests: IBM, TCS NQT, etc.)

In many online assessments you read the input yourself with `input()` and print the answer. Everything arrives as a **string**, so convert it.

> Each code block below has a `# stdin:` comment showing the sample input. `|` means "next line". In a real test the input comes from the judge.

## Cheat-sheet

| Input looks like | Code |
|---|---|
| One integer `5` | `n = int(input())` |
| One word / sentence | `s = input().strip()` |
| Two ints on one line `7 8` | `a, b = map(int, input().split())` |
| A list on one line `3 4 5` | `nums = list(map(int, input().split()))` |
| Count then list (2 lines) | `n = int(input())` then `nums = list(map(int, input().split()))` |
| Matrix of `r` rows | `[list(map(int, input().split())) for _ in range(r)]` |

## One integer

```python
# stdin: 5
n = int(input())
print(n * 2)
```

Output:

```text
10
```

## Two integers on one line

```python
# stdin: 7 8
a, b = map(int, input().split())
print(a + b)
```

Output:

```text
15
```

## A list on one line

```python
# stdin: 3 4 5
nums = list(map(int, input().split()))
print(nums, sum(nums))
```

Output:

```text
[3, 4, 5] 12
```

## Count first, then the list

```python
# stdin: 3|10 20 30
n = int(input())
nums = list(map(int, input().split()))
print(n, nums)
```

Output:

```text
3 [10, 20, 30]
```

## A sentence

```python
# stdin: hello big world
s = input().strip()
words = s.split()
print(words, len(words))
```

Output:

```text
['hello', 'big', 'world'] 3
```

## A matrix

```python
# stdin: 2|1 2|3 4
rows = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]
print(matrix)
```

Output:

```text
[[1, 2], [3, 4]]
```

## Printing the answer

```python
nums = [1, 2, 3]
print(nums)
print(*nums)
print(" ".join(map(str, nums)))
print(*nums, sep=", ")
```

Output:

```text
[1, 2, 3]
1 2 3
1 2 3
1, 2, 3
```

Read the sample output in the question carefully: brackets or no brackets, spaces or commas, one line or many. Judges compare text exactly.

## Common mistakes

- Forgetting `int(...)`: `"3" + "4"` is `"34"`, not 7.
- `input().split()` gives strings; wrap with `map(int, ...)` for numbers.
- Printing extra text like `"Answer:"` when the question wants only the value.
- Leaving debugging `print`s in the final submission.
