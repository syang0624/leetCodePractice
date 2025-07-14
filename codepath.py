class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mystery_function(head):
    if not head or not head.next:
        return head 

    prev = None
    tail = head
    while tail.next:
        prev = tail
        tail = tail.next

    if not prev:
        return head  
        
    tail.next = head.next
    prev.next = head
    head.next = None

    return tail


# Input List: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = mystery_function(head)