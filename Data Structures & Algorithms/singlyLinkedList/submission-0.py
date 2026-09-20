class Node:

    def __init__(self, value, nextNode=None):
        self.val = value
        self.next = nextNode
        



class LinkedList:
    
    def __init__(self):

        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:

        node = self.head.next
        i = 0
        while node:
            if i == index:
                return node.val
            i += 1
            node = node.next

        return -1
        

    def insertHead(self, val: int) -> None:

        new = Node(val, self.head.next)
        self.head.next = new

        if new.next is None:
            self.tail = new

        

    def insertTail(self, val: int) -> None:

        self.tail.next = Node(val)
        self.tail = self.tail.next

        
        

    def remove(self, index: int) -> bool:

        prev = self.head
        i = 0
        while prev.next:
            if i == index:
                if prev.next is self.tail:
                    self.tail = prev
                prev.next = prev.next.next
                return True
            i += 1
            prev = prev.next
        return False
            

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
