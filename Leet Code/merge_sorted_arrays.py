def mergeTwoLists(list1, list2):
        start = list1
        itr2 = list2
        if list1 and list2 and list1.val > list2.val:
            start = list2
            itr2 = list1
        
        head = start
        while start and start.next:
            if itr2 and start.next.val > itr2.val:
                start.next, itr2 = itr2, start.next
            start = start.next
        
        start.next = itr2
        
        return head


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)

list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(4)

print(mergeTwoLists(list1, list2))
    