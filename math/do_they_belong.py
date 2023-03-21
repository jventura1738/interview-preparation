import math
METADATA = {
    "name": "do_they_belong",
    "company": "Citadel",
    "tags": ["math", "geometry", "triangles"],
}

"""
PROMPT:
Given a triangle formed by a(x1, y1), b(x2, y2), c(x3, y3), and 
two points p(xp, yp) and q(xq, yq), return the correct scenario:

- 0: if the triangle forms a non-degenerate triangle
- 1: if p is inside the triangle but q is not
- 2: if q is inside the triangle but p is not
- 3: if both p and q are inside the triangle
- 4: if both p and q are outside the triangle

NOTE: a degenerate triangle is a triangle with zero area.

Author: Justin Ventura
"""


# distance between two points:
def distance(x1, y1, x2, y2) -> float:
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# area of triangle with 3 points:
def area(x1, y1, x2, y2, x3, y3):
    return abs(x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1) / 2


# returns true if area is 0 false otherwise
def is_degenerate(x1, y1, x2, y2, x3, y3) -> bool:
    ab = distance(x1, y1, x2, y2)
    ac = distance(x1, y1, x3, y3)
    bc = distance(x2, y2, x3, y3)
    return False if ab + bc > ac and bc + ac > ab and ab + ac > bc else True


# Check the scenarios:
def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq) -> int:
    if is_degenerate(x1, y1, x2, y2, x3, y3):
        return 0

    # we know p is in abc if areas of abp + apc + pab == area of abc
    p_is_inside = (area(x1, y1, x2, y2, xp, yp) + area(x1, y1, xp, yp, x3, y3) +
                   area(xp, yp, x2, y2, x3, y3)) == area(x1, y1, x2, y2, x3, y3)
    q_is_inside = (area(x1, y1, x2, y2, xq, yq) + area(x1, y1, xq, yq, x3, y3) +
                   area(xq, yq, x2, y2, x3, y3)) == area(x1, y1, x2, y2, x3, y3)

    if p_is_inside and q_is_inside:
        return 3
    if p_is_inside:
        return 1
    if q_is_inside:
        return 2
    return 4


if __name__ == "__main__":
    # Now some test cases:
    assert (pointsBelong(2, 2, 7, 2, 5, 4, 4, 3, 7, 10) == 1)
    assert (pointsBelong(2, 2, 7, 2, 5, 4, 4, 3, 5, 3) == 3)
    assert (pointsBelong(2, 2, 7, 2, 5, 4, 0, 0, 4, 2) == 2)
    assert (pointsBelong(2, 2, 7, 2, 5, 4, 0, 0, 4, 6) == 4)
