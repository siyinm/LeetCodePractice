Given a binary tree, return the inorder traversal of its nodes' values.

Example:

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

### Solution

1. 递归

2. 其核心思想如下：

   使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
   如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
   如果遇到的节点为灰色，则将节点的值输出。


   