# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n : return head
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        for i in range(m-1):
            left = left.next
        pre = None
        cur = left.next
        for j in range(n-m+1):
            if not cur:
                temp = None
            else:
                temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        left.next.next = cur
        left.next = pre
        return dummy.next
