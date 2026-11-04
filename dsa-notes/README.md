# DSA and Python Notes

My notes from learning Python and data structures and algorithms for placement preparation. Every code block in these notes was run and the output shown is the real output.

## How the notes are organised

| Folder | What is inside |
|---|---|
| [`01-python-foundations`](01-python-foundations) | loops and `range`, functions, lists/strings/dicts/sets, input handling, classes |
| [`02-core-patterns`](02-core-patterns) | accumulator, track-the-best, digit walker, frequency counting, hashing, prefix/suffix |
| [`03-searching-and-sorting`](03-searching-and-sorting) | linear and binary search, five sorting algorithms, Big O |
| [`04-two-pointers`](04-two-pointers) | opposite ends, slow and fast pointers |
| [`05-sliding-window`](05-sliding-window) | fixed and variable windows |
| [`06-linked-lists`](06-linked-lists) | node, build, traverse, insert, reverse, delete, next-up problems |
| [`07-practice-problems`](07-practice-problems) | HCF, decimal to binary, Fibonacci, Caesar shift, input-style assessment problems |

## Suggested order

1. Python foundations → core patterns
2. Searching and sorting
3. Two pointers → sliding window
4. Linked lists
5. Practice problems, until you can solve them without looking

## Pattern cheat-sheet

| If the problem says... | Think |
|---|---|
| count / most frequent / seen before / pair with a target (unsorted) | dictionary or set |
| sorted array, pair, palindrome | two pointers from both ends |
| in place, remove, move to the end | slow and fast pointers |
| subarray / substring of size k | fixed sliding window |
| longest / shortest subarray or substring with a rule | variable sliding window |
| sorted + "find / insert position" | binary search |
| everything except me, range sums | prefix / suffix |
| reverse / delete / middle in a linked list | pointers: `prev`, `current`, `next_node`, slow/fast |

## Habits that fixed my bugs

- Initialise every pointer and counter before the loop.
- `==` compares, `=` assigns.
- `return` the answer; don't just `print` it.
- Save `next_node` before changing a link.
- Test the sample, then empty, one item, and all-the-same inputs.

## Running the code

Every block is plain Python 3. Copy a block into a `.py` file and run `python file.py`. Blocks inside one file sometimes build on earlier blocks in the same file (for example the `Node` class), and blocks with a `# stdin:` comment expect that text as input (`|` means a new line).

## Uploading to GitHub

```bash
cd notes
git init
git add .
git commit -m "Add DSA and Python notes"
git branch -M main
git remote add origin https://github.com/athul-dotcom/<your-repo-name>.git
git push -u origin main
```

Create the empty repository on GitHub first (no README, so it doesn't clash), then paste its URL in the `remote add` line.
