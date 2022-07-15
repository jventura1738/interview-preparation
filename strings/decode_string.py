# Justin Ventura

'''
Google Interview Question
'''


# Solution:
def decodeString(s: str) -> str:
    stack = list()
    for idx in range(len(s)):
        if s[idx] != ']':
            stack.append(s[idx])

        # This is the case where we encounter a subproblem:
        else:
            sbuffer, nbuffer = list(), list()
            while stack[-1] != '[':
                sbuffer.append(stack.pop())
            stack.pop()  # get rid of ‘[’

            while len(stack) > 0 and stack[-1].isdigit():
                nbuffer.append(stack.pop())

            # Here we have completed the sub problem:
            # (reversed because stack is LIFO)
            pattern = ''.join(reversed(sbuffer))
            times = int(''.join(reversed(nbuffer)))
            for _ in range(times):
                stack.append(pattern)

    return ''.join(stack)


# Tests:
if __name__ == '__main__':
    assert decodeString('3[a]2[bc]') == 'aaabcbc'
    assert decodeString('3[a2[c]]') == 'accaccacc'
    assert decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef'
