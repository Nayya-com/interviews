from src.node import Node

class Cache:
    def __init__(self, maxSize) -> None:
        self.head = None
        self.tail = None
        self.currentSize = 0
        self.maxSize = maxSize
        self.lookupTable = {}

    def move_to_tail(self, key):
        node = self.lookupTable[key]
        # Remove node from current place
        if node == self.tail:
            return

        if node == self.head:
            self.head = node.nextNode
            node.prevNode = None
        else:
            left = node.prevNode
            right = node.nextNode
            left.nextNode = right
            right.prevNode = left

        # add node at tail
        before_tail = self.tail.prevNode
        tail = self.tail
        tail.nextNode = node
        node.prevNode = tail
        node.nextNode = None
        self.tail = node

    def remove_from_head(self, key):
        # Note: copied from above
        node = self.lookupTable[key]
        self.head = node.nextNode
        self.prevNode = None
        # This part is only difference from above
        del self.lookupTable[key]

    def get(self, key) -> int:
        if None == key:
            return None

        if key not in self.lookupTable.keys():
            return None

        result = self.lookupTable[key]        
        if self.tail is result:
            return result.value

        self.move_to_tail(key)

        # if None == result.prevNode:
        #     self.head = result.nextNode
        #     self.head.prevNode = None        

        # self.tail.nextNode = result
        # result.nextNode = None
        # result.prevNode = None
        # self.tail = result
        # return result.value

    def put(self, key, val) -> None:
        if None == key:
            return None
        
        newNode = Node(key, val, self.tail, None)
        if None == self.tail:
            self.head = newNode
        else:
            self.tail.nextNode = newNode
        
        self.tail = newNode
        self.lookupTable[key] = newNode

        self.move_to_tail(key)
        self.currentSize += 1
        if self.currentSize > self.maxSize:
            self.remove_from_head(key)
            self.currentSize -= 1

        # self.currentSize += 1
        # if self.currentSize > self.maxSize:
        #     self.lookupTable.pop(self.head.key)
        #     self.head = self.head.nextNode
        #     self.head.prevNode = None
        #     self.currentSize -= 1
        
        # newNode = Node(key, val, self.tail, None)
        # if None == self.tail:
        #     self.head = newNode
        # else:
        #     self.tail.nextNode = newNode
        
        # self.tail = newNode
        # self.lookupTable[key] = newNode

    def toArray(self):        
        a = []
        current = self.head
        while None != current:
            a.append(current.value)
            current = current.nextNode
        
        return a
