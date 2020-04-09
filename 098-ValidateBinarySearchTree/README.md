Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

### Solution

**解法1**

中序遍历结果为递增数列

**解法2**

递归遍历整个树，在遍历树的同时保留结点的上界与下界，在比较时不仅比较子结点的值，也要与上下界比较。