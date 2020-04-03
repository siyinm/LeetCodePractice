Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

### Solution

对于reverse linked list 1来说，需要

1. 找到被逆转的节点头部
2. 用第206题的方法逆转链表
3. 将被逆转部分的头尾接回原来的链表

很多边界问题需要处理





链表太搞了