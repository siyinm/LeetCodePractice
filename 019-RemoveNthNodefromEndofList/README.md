## Remove Nth Node from End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
```{}
Given linked list: 1->2->3->4->5, and n = 2.
```
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

### Solution
利用间隔为n的**双指针**一次遍历实现 O(n)

list: dummyhead （处理出现返回空节点的情况）