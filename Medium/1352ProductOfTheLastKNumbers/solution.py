class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.prefix.append(self.prefix[-1]*num)
        else:
            self.prefix=[1]

    def getProduct(self, k: int) -> int:
        self.size  = len(self.prefix) - 1
        if k > self.size:
            return 0
        return self.prefix[self.size] // self.prefix[self.size - k]
    
# Time Complexity: O(1)
# Space Complexity: O(N)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)