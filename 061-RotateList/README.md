## Rotate List

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

```{}
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
```

### Solution:

1. 先遍历一遍得到长度n

2. list 收尾相连

3. 在n-k断开

