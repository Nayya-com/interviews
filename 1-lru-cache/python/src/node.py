class Node:
    def __init__(self, key, value, prevNode, nextNode) -> None:
        self.key = key
        self.value = value        
        self.prevNode = prevNode
        self.nextNode = nextNode
    
    def __repr__(self):
        return f"Node({self.key=},{self.value=})"
