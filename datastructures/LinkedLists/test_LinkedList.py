# Justin Ventura

'''Testing for linkedlists.py'''
from LinkedList import *


# Test the append function:
def test_append() -> None:
    '''Test the append function.'''
    head = None
    head = append(head, 1)
    head = append(head, 2)
    head = append(head, 3)
    head = append(head, 4)
    head = append(head, 5)
    result = lprint(head)
    assert result == [1, 2, 3, 4, 5]


# Test the insert_at function:
def test_insert_at() -> None:
    '''Test the insert_at function.'''
    head = None
    head = insert_at(head, 0, 1)
    head = insert_at(head, 0, 2)
    head = insert_at(head, 0, 3)
    head = insert_at(head, 0, 4)
    head = insert_at(head, 0, 5)
    result = lprint(head)
    assert result == [5, 4, 3, 2, 1]

    # head = None
    # head = insert_at(head, 1, 1)
    # head = insert_at(head, 1, 2)
    # head = insert_at(head, 1, 3)
    # head = insert_at(head, 1, 4)
    # head = insert_at(head, 1, 5)
    # result = lprint(head)
    # assert result == [1, 5, 4, 3, 2]
