# from collections import defaultdict
# class Villager:
#     valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
#     def __init__(self, name, species, personality, catchphrase):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []

#     def add_item(self, item_name):
#         if item_name in self.valid:
#             self.furniture.append(item_name)


# def of_personality_type2(townies, personality_type):
#     res = []
#     for item in townies:
#         if item.personality == personality_type:
#             res.append(item.name)
#     return res


# personalities = defaultdict(list)

# def of_personality_type(townies, personality_type):
#     for townie in townies:
#         personalities[townie.personality].append(townie.name)
#     return personalities[personality_type]

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))
# print(of_personality_type([], "Cranky"))


# from collections import defaultdict
# class Villager:
#     def __init__(self, name, species, personality, catchphrase, neighbor=None):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.neighbor = neighbor

# def message_received(start_villager, target_villager) -> bool:
#     if start_villager is None:
#         return False
#     if start_villager == target_villager:
#         return True
#     else:
#         return message_received(start_villager.neighbor, target_villager)


# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# isabelle = Node("Isabelle")
# saharah = Node("Saharah", isabelle)
# harriet = Node("Harriet", saharah)
# kk_slider = Node("K.K. Slider", harriet)



# print_linked_list(kk_slider)

# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def catch_fish(head):
#     if head is None:
#         print("Aw! Better luck next time!")
#         return
#     print(f"I caught a {head.fish_name}!")
#     head = head.next
#     return head

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))

# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next


# def fish_chances(head, fish_name):
    
#     total_count = 0

#     def helper(head):
#         nonlocal total_count
#         if not head:
#             return 0
#         total_count += 1
#         return helper(head.next) + (1 if head.fish_name == fish_name else 0)
    
#     return round(helper(head) / total_count, 2)
# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))
# head = Node("Isabelle", Node("Alfonso"))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

