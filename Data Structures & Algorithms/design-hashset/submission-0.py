class MyHashSet:

    def __init__(self):
        self.nums = [[]for _ in range(0,10)]
        

    def add(self, key: int) -> None:
        
        index = key % 10

        if key not in self.nums[index]:
            self.nums[index].append(key)

        

    def remove(self, key: int) -> None:
        index = key % 10
        if key in self.nums[index]:
            self.nums[index].remove(key)
         

        

    def contains(self, key: int) -> bool: 
        index = key % 10

        return key in self.nums[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)