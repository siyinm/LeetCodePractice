Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

        3
        / \
      9  20
        /  \
       15   7
   

### Solution

bfs遍历

解决每一层如何分开？

大循环里套小循环，每层新建一个队列存放一层的元素

运用两个队列区分当前层和下一层的元素，遍历当前层元素，新元素放入next队列里

当前层队列空了，就结束小循环，将next队列赋给当前层队列，进入下一个大循环

