Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

```
Input: 1->2->3->3->4->4->5
Output: 1->2->5
```

### Solution

Use dummy head

take care of the situation `[1,1,1]`, 最后删除节点的时候