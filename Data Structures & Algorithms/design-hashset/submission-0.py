class MyHashSet:

    def __init__(self):
        self.arr = [0] * 10000

    def add(self, key: int) -> None:
        idx = key % 10000
        self.arr[idx] = key

    def remove(self, key: int) -> None:
        idx = key % 10000
        self.arr[idx] = 0

    def contains(self, key: int) -> bool:
        return self.arr[key % 10000] != 0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)