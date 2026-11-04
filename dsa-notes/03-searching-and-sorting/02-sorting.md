# Sorting algorithms

Every example sorts the same list so you can compare: `[64, 25, 12, 22, 11, 5]` → `[5, 11, 12, 22, 25, 64]`.

## Bubble sort: O(n²)

Repeatedly swap neighbours that are in the wrong order. After pass `i`, the `i` largest items are in place at the end, so the inner loop can be shorter each time.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([64, 25, 12, 22, 11, 5]))
```

Output:

```text
[5, 11, 12, 22, 25, 64]
```

## Selection sort: O(n²)

Find the smallest item in the unsorted part and put it at the front.

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11, 5]))
```

Output:

```text
[5, 11, 12, 22, 25, 64]
```

## Insertion sort: O(n²), fast on nearly-sorted data

Take the next item (`key`) and slide it left into its place among the already-sorted items, like sorting playing cards in your hand.

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([64, 25, 12, 22, 11, 5]))
```

Output:

```text
[5, 11, 12, 22, 25, 64]
```

## Merge sort: O(n log n), extra O(n) space

Split in half, sort each half (recursively), then **merge** two sorted halves.

```python
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

print(merge_sort([64, 25, 12, 22, 11, 5]))
```

Output:

```text
[5, 11, 12, 22, 25, 64]
```

The `merge` step is itself a two-pointer idea (one pointer per half).

## Quick sort: O(n log n) average, O(n²) worst case

Pick a pivot, move smaller items to its left and bigger to its right (`partition`), then sort each side.

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        quick(arr, low, p - 1)
        quick(arr, p + 1, high)
    return arr

print(quick([64, 25, 12, 22, 11, 5]))
```

Output:

```text
[5, 11, 12, 22, 25, 64]
```

## Python's built-in sort

In real code and in LeetCode, use these. They are O(n log n) (Timsort).

```python
nums = [64, 25, 12, 22, 11, 5]
print(sorted(nums))
print(sorted(nums, reverse=True))
words = ["pear", "fig", "banana"]
words.sort(key=len)
print(words)
```

Output:

```text
[5, 11, 12, 22, 25, 64]
[64, 25, 22, 12, 11, 5]
['fig', 'pear', 'banana']
```

## Summary table

| Sort | Best | Average | Worst | Extra space | Idea |
|---|---|---|---|---|---|
| Bubble | O(n²)* | O(n²) | O(n²) | O(1) | swap neighbours |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | pick the minimum |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | slide into place |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | split, sort, merge |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | pivot + partition |

\* O(n) if you add a "no swaps happened, stop" flag.
