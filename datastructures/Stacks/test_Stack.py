# Justin Ventura


from Stack import *


# Test the push function:
def test_push() -> None:
    '''Test the push function.'''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    result = stack.sprint()
    assert result == [1, 2, 3, 4, 5]


# Test the pop function:
def test_pop() -> None:
    '''Test the pop function.'''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    result = list()
    while not stack.is_empty():
        result.append(stack.pop())
    assert result == [5, 4, 3, 2, 1]
