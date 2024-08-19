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

    def remove_from_head(self):
        # Note: copied from above
        key = self.head.key

        right = self.head.nextNode
        self.head = right
        right.prevNode = None

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
            self.remove_from_head()
            self.currentSize -= 1

    def toArray(self):        
        a = []
        current = self.head
        while None != current:
            a.append(current.value)
            current = current.nextNode
        
        return a
