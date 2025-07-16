# def count_layers(sandwich):
    
#     if len(sandwich) == 1:
#         return 1
    

#     return 1 + count_layers(sandwich[1])


# '''
# Input: Nested List

# Out: Number of Layers (Int)
# '''

# sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
# sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))

# def reverse_orders(orders):
#     lst = orders.split(" ")
#     if len(lst) == 1:
#         return lst[0]
#     last = lst[-1]
#     lst.pop()
#     return last + " " + reverse_orders(" ".join(lst))


# print(reverse_orders("Bagel Sandwich Coffee"))


# def can_split_coffee(coffee, n):
#     if len(coffee) == 1:
#         if coffee[0] % n == 0:
#             return True
#         return False
#     element = coffee[0]
#     if element % n != 0:
#         return False
#     return can_split_coffee(coffee[1:], n)

# print(can_split_coffee([4, 4, 8], 2))
# print(can_split_coffee([5, 10, 15], 4))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    if not sandwich_a:
        return sandwich_b
    if not sandwich_b:
        return sandwich_a

    nodeA = sandwich_a
    nextNodeA = sandwich_a.next
    nodeB = sandwich_b
    nextNodeB = sandwich_b.next
    nodeA.next = nodeB
    nodeB.next = merge_orders(nextNodeA, nextNodeB)
    return nodeA

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

# print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))