# The Millionth Fibonnacci Kata

## Attempt 1
### Solving Recurrence Relations Condition
We know that the Fibonacci sequence is a linear homogeneous recurrence relation with a constant coefficient.

Linear: Fibonacci is just an addition of multiple numbers like `fn = fn-1 + fn-2` (Pick any n and decompose the reccurences and you will still have an addition)

Constant Coefficients: All coefficients have no dependency to n (here c1 = c2 = 1 in fn = c1fn-1 + c2fn-2).

Homogeneous: Every term have the same degree

### Solution (Too slow)
We can transform the fibonacci sequence `fn = fn-1 + fn-2`:


```
fn - fn-1 - fn-2 = 0
fn+2 - fn+1 - fn = 0
```

With that we can easily see a characteristic equation like this:
`r^2 - r - 1 = 0`

This is a simple quadratic equation which (I will not put the steps here, you should use wolframalpha) is solved with:

```
r0 = (1 - sqrt(5))/2
r1 = (1 + sqrt(5))/2
```

The solution has now this form:
```
fn = b((1+sqrt(5))/2)^n + d((1-sqrt(5))/2)^n
```

Python solution (still too slow):
```python
from math import sqrt

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if n > 0:
        return fib_(n)
    if n < 0:
        return fib(n + 2) - fib(n + 1)

def fib_(n):
    b, d = 1/sqrt(5), -1/sqrt(5)
    a1, a2 = (1 + sqrt(5)) / 2, (1 - sqrt(5)) / 2
    return round(b * pow(a1, n) - d * pow(a2, n))
```
