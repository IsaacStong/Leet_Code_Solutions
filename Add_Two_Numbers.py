"""Created by Isaac Stong on 6/17/20
    Given two singly linked list sum the reverse of those linked lists
    Store result in same manner.
    Ex. (2 -> 4 -> 3) + (5 -> 6 -> 4) = 7 -> 0 -> 8
    Explanation 342 + 465 = 807"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def add_two_numbers(l1, l2):
    num1 = list_to_int(l1)
    num2 = list_to_int(l2)
    sum = num1 + num2
    temp = None
    for i in str(sum):
        temp = ListNode(int(i), temp)
    return temp


def list_to_int(l1):
    if l1.next is None:
        return l1.val
    else:
        return l1.val + (10*list_to_int(l1.next))


b1 = ListNode(6)
b2 = ListNode(2, b1)
b3 = ListNode(3, b2)
a1 = ListNode(3)
a2 = ListNode(2, a1)
a3 = ListNode(1, a2)
lel = add_two_numbers(b3, a3)

for i in range(3):
     print(lel.val)
     lel = lel.next

