Reverse a singly linked list.

Example:

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

### Solution

申请两个指针，

第一个指针叫 pre，最初指向 null 。

第二个指针 cur 指向 head

遍历每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 同时前进一位。

结束条件为cur 变成 null ，pre 是最后一个节点。
