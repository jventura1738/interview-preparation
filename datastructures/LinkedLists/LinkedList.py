# Justin Ventura

'''This is the module for linked list api.'''
from typing import List


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = None


# This is the low IQ O(n) append:
def append(head: ListNode = None, value: any = 0) -> ListNode:
    '''Append a value to the end of a linked list.'''
    new_node = ListNode(x=value, next=None)

    # Edge case, no head.
    if not head:
        return new_node

    trav = head
    while trav.next:  # O(n)
        trav = trav.next
    trav.next = new_node
    return head


# Insert a value at a specific index:
def insert_at(head: ListNode = None, index: int = 0,
              value: any = 0) -> ListNode:
    '''Insert a value at a specific index of a linked list.'''
    new_node = ListNode(x=value, next=None)

    # Edge case, no head.
    if not head:
        return new_node

    # Edge case, insert at front.
    if index == 0:
        new_node.next = head
        return new_node

    trav = head
    for _ in range(index - 1):  # O(n)
        # Catch out of bounds.
        try:
            trav = trav.next
        except AttributeError:
            return head
    new_node.next = trav.next
    trav.next = new_node
    return head


# Insert a value in a sorted order:
def insert(head: ListNode = None, value: any = 0) -> ListNode:
    '''Insert a value in the list in an ascending sorted order.

    Note that custom types must have operators overloaded, and
    the list node values must be of the same type.  This also
    assumes that the list is already sorted.'''
    new_node = ListNode(x=value, next=None)

    # Edge case, no head.
    if not head:
        return new_node

    # Edge case, insert at front:
    try:
        if new_node.val < head.val:
            new_node.next = head

        trav = head
        while trav.next and trav.val >= new_node.val:
            trav = trav.next
        new_node.next = trav.next
        trav.next = new_node
        return head

    # Catch non-matching types.
    except TypeError:
        return head


# Remove the first instance of a value:
def remove(head: ListNode = None, value: any = None) -> ListNode:
    '''Remove the first instance of value in the list.'''
    # Edge case, no head.
    if not head:
        return head

    # Find value to remove in the list:
    trav = head
    prev = None
    while trav.next and trav.val != value:
        prev = trav
        trav = trav.next
    # Edge case, value not found.
    if trav.val != value:
        return head

    # Remove value:
    if prev:
        prev.next = trav.next
    else:
        head = trav.next
    return head


# Print a linked list:
def lprint(head: ListNode = None) -> List[any]:
    '''Print a linked list.'''
    values_list = []
    trav = head
    while trav:
        values_list.append(trav.val)
        print(trav.val)
        trav = trav.next
    return values_list
