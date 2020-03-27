# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        search = head.next
        curr = head
        while search:
            if search.val == curr.val:
                search = search.next
            else: 
                curr.next = search 
                curr = curr.next
                search = search.next
        curr.next = None
        return head
