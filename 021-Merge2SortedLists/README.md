## Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

```{}
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

### Solution

1. 迭代

   （为了避免递归）我用的这个方法， 官方说是迭代就是吧

   新建一个head, head->next 指向l1, l2中更小的那一个，指完next一下

   记得在开始处理一方为空list的情况 

2. 递归

   $\left\{\begin{array}{ll}{ \text { list }[0]+\text { merge (list1[ } 1:], \text { list2 })} & {\text { list1 }[0]<\text { list } 2[0]} \\ {\text { list2 }[0]+\text { merge(list1, list2[1: :)) }} & {\text { otherwise }}\end{array}\right.$

   记得在开始处理一方为空list的情况 此处也是一种停止条件

3. 插入法

   先判断头，再向一个list中插入另一list，比较复杂