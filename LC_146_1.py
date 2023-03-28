'''
Use OrderedDict() method to solve; runtime complexity is O(n), space complexity is O(n); n is capacity
'''

#from collections import deque
from collections import OrderedDict
class LRUCache:
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
    def __init__(self, capacity: int):
        self.c=capacity
        self.dic=OrderedDict()
    
    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic[key]=self.dic.pop(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> int:
        self.dic.__setitem__(key, value)
        self.dic[key]=self.dic.pop(key)
        if len(self.dic)>self.c: self.dic.popitem(last=False)
        #print(self.dic)


#Normal way to solve, use list for order; use dictionary for hashmap data
#runtime complexity is O(n), space complexity is O(n), n is capacity(input)
#Note: remove is left del first match item, deque.popleft(no input) just can del the leftst item
'''
    def __init__(self, capacity: int):
        self.c=capacity
        self.dic={}
        self.ll=[]

    def get(self, key: int) -> int:
        if key in self.dic:
            self.ll.remove(key)
            self.ll.append(key)
            return self.dic[key]
        else: return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key]=value
            self.ll.remove(key)
            self.ll.append(key)
        else:
            if len(self.ll)<self.c:
                self.ll.append(key)
                self.dic[key]=value
            else:
                del self.dic[self.ll[0]]
                self.ll=self.ll[1:]
                self.ll.append(key)
                self.dic[key]=value
        #print(self.ll)
'''