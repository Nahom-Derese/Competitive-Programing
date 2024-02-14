
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1List = ''
        l2List = ''
        for itr in [l1,l2]:
            if itr == l1:
                while itr.next != None:
                    l1List += str(itr.val)
                    itr = itr.next
                l1List += str(itr.val)
            else:
                while itr.next != None:
                    l2List += str(itr.val)
                    itr = itr.next
                l2List += str(itr.val)
        num1 = int(l1List[::-1])
        num2 = int(l2List[::-1])
        
        itrator = ListNode()
        ans = itrator
        x = str(num1+num2)[::-1]
        for i in range(len(x)):
            itrator.val = int(x[i])
            if i == len(x)-1:
                break
            itrator.next = ListNode()
            itrator = itrator.next

        return ans


L1 = ListNode(2,ListNode(4,ListNode(9)))
L2 = ListNode(5,ListNode(6,ListNode(4,ListNode(9))))

answer = Solution.addTwoNumbers(L1,L2)
        
while answer.next != None:
    print(answer.val)
    answer = answer.next
print(answer.val)