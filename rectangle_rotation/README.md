# Instructions
## Task

A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane. Its center (the intersection point of its diagonals) coincides with the point (0, 0), but the sides of the rectangle are not parallel to the axes; instead, they are forming `45 degree` angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?
## Example

For `a = 6 and b = 4`, the output should be `23`

The following picture illustrates the example, and the 23 points are marked green.

![img](https://raw.githubusercontent.com/serafss2/codewars_python/tree/master/rectangle_rotation/img1.png)

## Input/Output

    `[input]` integer `a`

    A positive `even` integer.

    Constraints: `2 ≤ a ≤ 10000`.

    `[input]` integer `b`

    A positive `even` integer.

    Constraints: `2 ≤ b ≤ 10000`.

    `[output]` an integer

    The number of inner points with integer coordinates.

# Attempt 1

```python
from math import sqrt, ceil, floor
def rectangle_rotation(a, b):
    return ceil(a/sqrt(2)) * ceil(b/sqrt(2)) + floor(a/sqrt(2)) * floor(b/sqrt(2))
```

Issue with this attempt seems to be precision? Every not working test has a gap of +1: `Your result is: 8090128 should equal 8090127`, `Your result is: 45661538 should equal 45661537` etc