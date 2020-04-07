Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

### Solution

动态规划

理解： n个nodes 的二叉树 可以分为以1:n为顶点的n种情况

而对于以数字i为顶点的情况，其左子树节点个数为i-1个，右子树节点为n-i，(二叉树性质)

所以可以列出式子
$$
G(n)=f(1)+f(2)+f(3)+f(4)+\ldots+f(n)
$$

$$
f(i)=G(i-1) * G(n-i)
$$

最后得到表达式
$$
G(n)=G(0) * G(n-1)+G(1) *(n-2)+\ldots+G(n-1) * G(0)
$$
若是计算可得**卡塔兰数**公式
$$
C_{0}=1, \quad C_{n+1}=\frac{2(2 n+1)}{n+2} C_{n}
$$
