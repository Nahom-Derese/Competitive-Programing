class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        dummy = Node(None)
        dummy.next = self.head
        temp = dummy
        
        count = 0
        while temp and count < index + 1:
            count+=1
            temp=temp.next
        
        if temp:
            return temp.val
        return -1


    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        dummy = Node(None)
        node = Node(val)

        dummy.next = self.head
        temp = dummy

        while temp.next:
            temp = temp.next
        temp.next=node
        self.head = dummy.next



    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(None)
        node = Node(val)
        dummy.next = self.head
        
        temp = dummy
        count = 0
        while temp and count < index:
            temp=temp.next
            count+=1

        if temp:
            node.next = temp.next
            temp.next = node
            self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(None)
        dummy.next = self.head
        temp = dummy
        count = 0
        while temp and temp.next and count < index:
            temp=temp.next
            count+=1
        if temp and temp.next:
            temp.next = temp.next.next
            self.head = dummy.next


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)