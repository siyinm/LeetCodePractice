# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0: return l2
        if l2.val == 0: return l1
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        ONE = False
        dummy = ListNode(-1)
        curr = ListNode(0)
        dummy = curr
        
        while l1 or l2 or ONE:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            su = val1 + val2 +1 if ONE else val1 + val2
            node = ListNode(su % 10)
            curr.next = node
            curr = node
            if su>=10:
                ONE = True
            else:
                ONE = False
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            
        return self.reverseList(dummy.next)


    def reverseList(self, head: ListNode) -> ListNode:
        fi = None
        se = head
        while se:
            t = se.next
            se.next = fi
            fi = se
            se = t
        return fi
