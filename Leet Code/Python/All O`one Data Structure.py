class AllOne:
    def __init__(self):
        self.o = {}

    def inc(self, key: str) -> None:
        if self.o.get(key):
            self.o[key] += 1
        else:
            self.o[key] = 1
        

    def dec(self, key: str) -> None:
        if self.o.get(key) == 1:
            self.o.pop(key)
        else:
            self.o[key] -= 1
        

    def getMaxKey(self) -> str:
        pass
        

    def getMinKey(self) -> str:
        pass
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()