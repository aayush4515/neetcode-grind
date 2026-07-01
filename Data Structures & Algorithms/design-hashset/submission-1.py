class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        self.hashset.append(key) if key not in self.hashset else None

    def remove(self, key: int) -> None:
        self.hashset.remove(key) if key in self.hashset else None

    def contains(self, key: int) -> bool:
        print(f"Hash set before contains({key}) is called: {self.hashset}")
        res = False
        if key in self.hashset:
            res = True
        else:
            res = False
        
        return res


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)