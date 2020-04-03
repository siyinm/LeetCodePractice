# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        fi = None
        se = head
        while se:
            t = se.next
            se.next = fi
            fi = se
            se = t
        return fi
            
