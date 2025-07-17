from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        lTail, rTail = left, right
        while head:
            if head.val >= x:
                rTail.next = head
                rTail = rTail.next
            else:
                lTail.next = head
                lTail = lTail.next
            head = head.next
        
        lTail.next = right.next
        rTail.next = None
        return left.next

# Time Complexity: O(N)
# Space Complexity: O(N)