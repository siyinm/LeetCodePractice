A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

### Solution

类似求两个集合的交集算法，求线段交点/重合

- 一开始将集合表示出来，循环求交集判断元素>=1，超出时间限制

- 应该用边界条件判断，分类讨论或者，判断不重合情况再取逆更简单