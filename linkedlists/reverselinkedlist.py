# Justin Ventura

# Linked List:
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


# Reverse a linked list.
def reverseList(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


if __name__ == '__main__':
    curr = ListNode(1)
    head = curr
    for i in range(2, 6):
        curr.next = ListNode(i)
        curr = curr.next

    ll = reverseList(head)
    curr = ll
    while curr:
        print(curr.val, end=' ')
        curr = curr.next
    print()
