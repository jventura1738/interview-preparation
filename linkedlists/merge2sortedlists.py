# Justin Ventura

# Linked List:
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = None


# Merge 2 sorted lists:
def merge_two_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next

        tail = tail.next

    tail.next = l1 or l2
    return dummy.next


if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    ll = merge_two_sorted_lists(list1, list2)
    trav = ll
    while trav:
        print(trav.val)
        trav = trav.next
