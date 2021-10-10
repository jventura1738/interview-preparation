# Justin Ventura

import sys

"""
input reuonnoinfe should output 149
and reuveoninofinfe should output 1459
"""

nums = {
    'one': 0,
    'two': 0,
    'three': 0,
    'four': 0,
    'five': 0,
    'six': 0,
    'seven': 0,
    'eight': 0,
    'nine': 0
}

numerics = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
num_strings = ['one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine']

def print_result():
    res = []
    for num in nums.keys():
        i = nums[num]
        if i > 0:
            res += [numerics[num]]*i
    for r in res:
        print(r,end='')
    print()


def calc_results(shuffled):
    p = 0
    while len(shuffled) > 0:
        in_shuffle = True
        for c in num_strings[p]:
            if c not in shuffled:
                in_shuffle = False
        if in_shuffle:
            for c in num_strings[p]:
                shuffled = shuffled.replace(c, '', 1)
            nums[num_strings[p]] += 1
        p += 1
        if p == 9:
            p = 0

if __name__ == '__main__':
    shuffled = sys.argv[1]
    calc_results(shuffled)
    print_result()
