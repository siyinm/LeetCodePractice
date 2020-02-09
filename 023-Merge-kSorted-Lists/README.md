## Merge-k-Sorted-Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

```{python}
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

### Solution

1. 分治合并：类似并行
2. 两个合并的链表和下一个合并
3. 每次取链表第一个比较，最小的值加入新链表，空的链表删除