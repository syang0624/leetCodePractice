# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# # For testing
# def print_queue(head):
#     current = head.front
#     while current:
#         print(current.value, end=" -> " if current.next else "")
#         current = current.next
#     print()

# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
    
#     def is_empty(self):
#         return self.front is None

#     def enqueue(self, tup):
#         new_node = Node(tup)
#         if self.is_empty():
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             self.rear = new_node
    
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         value = self.front.value
#         self.front = self.front.next
#         return value
    
#     def peek(self):
#         return None if self.is_empty() else self.front.value


# # Create a new Queue
# q = Queue()

# # Add elements to the queue
# q.enqueue(('Love Song', 'Sara Bareilles'))
# q.enqueue(('Ballad of Big Nothing', 'Elliot Smith'))
# q.enqueue(('Hug from a Dinosaur', 'Torres'))
# print_queue(q)

# # View the front element
# print("Peek: ", q.peek()) 

# # Remove elements from the queue
# print("Dequeue: ", q.dequeue()) 
# print("Dequeue: ", q.dequeue()) 

# # Check if the queue is empty
# print("Is Empty: ", q.is_empty()) 

# # Remove the last element
# print("Dequeue: ", q.dequeue()) 

# # Check if the queue is empty
# print("Is Empty:", q.is_empty()) 

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# def merge_playlists(playlist1, playlist2, a, b):
#     temp = Node(0)
#     # count = 0
#     for i in range(b + 1):
#         if i <= a:
#             temp.next = playlist1
#             playlist1 = playlist1.next
#             temp = temp.next
#         elif playlist2.next is None:
#             temp.next = playlist1
#             playlist1 = playlist1.next
#             temp = temp.next
#         else:
#             temp.next = playlist2
#             playlist2 = playlist2.next
#             temp = temp.next

#     return temp.next


def merge_playlists(playlist1, playlist2, a, b):
    dummy = Node(0, playlist1)
    prev = dummy

    # Step 1: Traverse to the node just before position a
    for _ in range(a):
        prev = prev.next

    # Step 2: Traverse from prev to node at position b
    curr = prev
    for _ in range(b - a + 1):
        curr = curr.next

    # Step 3: Connect prev.next to playlist2
    prev.next = playlist2

    # Step 4: Traverse to the end of playlist2
    tail = prev
    while tail.next:
        tail = tail.next

    # Step 5: Connect tail of playlist2 to curr.next
    tail.next = curr.next

    return dummy.next


playlist1 = Node(('Flea', 'St. Vincent'),
                Node(('Juice', 'Lizzo'), 
                    Node(('Tenderness', 'Jay Som'),
                        Node(('Ego Death', 'The Internet'),
                            Node(('Empty', 'Kevin Abstract'))))))

playlist2 = Node(('Dreams', 'Solange'), Node(('First', 'Gallant')))

print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))