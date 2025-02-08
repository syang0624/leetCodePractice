from sortedcontainers import SortedSet

class NumberContainers:
    def __init__(self):
        self.index_number = {}  # Maps index to number
        self.number_indices = {}  # Maps number to sorted set of indices

    def change(self, index: int, number: int) -> None:
        # If the index is already in use, remove the old number
        if index in self.index_number:
            old_number = self.index_number[index]
            self.number_indices[old_number].discard(index)
            if not self.number_indices[old_number]:
                del self.number_indices[old_number]  # Remove if no indices left for the old number

        # Insert the new number
        self.index_number[index] = number
        if number not in self.number_indices:
            self.number_indices[number] = SortedSet()
        self.number_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.number_indices:
            return -1  # Number not found
        return self.number_indices[number][0]  # Return the smallest index
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)