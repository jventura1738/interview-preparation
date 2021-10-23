# Justin Ventura

"""
Count how many possible paths there are from the top left
corner to the bottom right corner.

(0, x) -> 0
(x, 0) -> 0
(1, 1) -> 1
(2, 3) -> 3
"""

import sys
from typing import Dict


def grid_traveler(rows: int, cols: int, memo: Dict) -> int:
    pass


if __name__ == '__main__':
    assert(len(sys.argv) == 3)
    grid_traveler(sys.argv[1:])
