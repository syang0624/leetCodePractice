from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        number = 0
        for i in range(len(stack)):
            s = stack.pop()
            number += s * (2**i)
        return number
