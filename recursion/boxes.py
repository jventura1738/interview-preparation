# Justin Ventura

def num_of_piles(n, m, p):
    return split(n//p, m, p, n%p)


# O(log_p(n)) TIME, O(n) stack frames SPACE?
def split(n, m, p, extra):
    piles = [n]*p
    for i in range(len(piles)):
        if extra > 0:
            piles[i] += 1
            extra -= 1
    total = 0
    for pile in piles:
        if pile <= m:
            total += 1 if pile != 0 else 0
        else:
            total += split(pile//p, m, p, pile%p)
    return total


if __name__ == '__main__':
    assert num_of_piles(11, 2, 2) == 7
    print(num_of_piles(11, 2, 2))
