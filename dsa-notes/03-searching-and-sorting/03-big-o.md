# Big O: how code grows as input grows

Big O describes how the work grows when `n` (input size) grows. Ignore constants and small terms: `3n + 5` is O(n).

| Big O | Name | Typical code | Example |
|---|---|---|---|
| O(1) | constant | direct access, arithmetic | `arr[i]`, dict lookup |
| O(log n) | logarithmic | halving each step | binary search |
| O(n) | linear | one loop | sum, linear search, Two Sum with dict |
| O(n log n) | linearithmic | sort | merge sort, `sorted()` |
| O(n²) | quadratic | loop inside loop | brute-force Two Sum, bubble sort |

## How to read your own code

- One loop over `n` → O(n).
- Two loops one after another → O(n) + O(n) = O(n).
- A loop inside a loop → O(n²).
- Loop that halves the range each time → O(log n).
- `x in list` inside a loop is a hidden second loop → O(n²). Use a `set` or `dict`.
- Space: count the extra structures you create (a dict of size n → O(n) space).

## Problems solved so far

| Problem | Time | Space |
|---|---|---|
| Two Sum (dict) | O(n) | O(n) |
| Binary search | O(log n) | O(1) |
| Move zeros / remove duplicates (two pointers) | O(n) | O(1) |
| Container With Most Water | O(n) | O(1) |
| Reverse linked list | O(n) | O(1) |
| Product of array except self | O(n) | O(1) extra |
