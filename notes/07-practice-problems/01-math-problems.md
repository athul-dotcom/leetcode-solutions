# Practice problems: math and number logic

## HCF (GCD) of two numbers

### Version 1: try every candidate from the top

The HCF can't be bigger than the smaller number. Count down from there; the first number that divides both is the answer.

```python
def hcf(a, b):
    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

print(hcf(12, 18), hcf(7, 13), hcf(100, 75))
```

Output:

```text
6 1 25
```

### Version 2: Euclid's algorithm (faster)

`hcf(a, b) = hcf(b, a % b)` until `b` is 0.

```python
def hcf_euclid(a, b):
    while b:
        a, b = b, a % b
    return a

print(hcf_euclid(12, 18), hcf_euclid(7, 13), hcf_euclid(100, 75))
```

Output:

```text
6 1 25
```

LCM follows from HCF: `lcm = a * b // hcf`.

```python
def lcm(a, b):
    return a * b // hcf_euclid(a, b)

print(lcm(4, 6))
```

Output:

```text
12
```

## Decimal to binary

Repeatedly divide by 2. The remainders, read **bottom to top**, are the binary digits. Collect the remainders, then reverse.

```python
def to_binary(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 2))
        n //= 2
    return "".join(reversed(digits))

print(to_binary(10), to_binary(0), to_binary(37))
print(bin(37)[2:])
```

Output:

```text
1010 0 100101
100101
```

Trace for 10: 10÷2 → r0, 5÷2 → r1, 2÷2 → r0, 1÷2 → r1. Remainders 0,1,0,1 reversed = `1010`.

Binary back to decimal:

```python
def to_decimal(bits):
    value = 0
    for b in bits:
        value = value * 2 + int(b)
    return value

print(to_decimal("1010"), int("100101", 2))
```

Output:

```text
10 37
```

## Fibonacci triangle

Each number is the sum of the previous two. Keep a list `fib`, then print the first `i` items on row `i`.

```python
fib = [0, 1]
for _ in range(10):
    fib.append(fib[-1] + fib[-2])

for i in range(1, 6):
    print(*fib[:i])
```

Output:

```text
0
0 1
0 1 1
0 1 1 2
0 1 1 2 3
```

First `n` Fibonacci numbers without a list (two variables):

```python
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(8))
```

Output:

```text
[0, 1, 1, 2, 3, 5, 8, 13]
```

## Armstrong, palindrome number, digit sum

All use the digit walker (see `02-core-patterns/01-accumulator-track-best-digits.md`).

```python
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

print(is_armstrong(153), is_armstrong(154), digit_sum(9875))
```

Output:

```text
True False 29
```
