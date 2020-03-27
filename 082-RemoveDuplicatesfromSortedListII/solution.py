# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        
        dummy= ListNode(0)
        dummy.next = head

        search = head.next
        curr = dummy
        flag = 1
        while search:
            if search.val == curr.next.val:
                search = search.next
                flag = 0
            else: 
                if flag: curr = curr.next
                curr.next = search
                search = search.next
                flag = 1
             
        if not flag: curr.next = None
        else: curr.next.next = None   
        return dummy.next
