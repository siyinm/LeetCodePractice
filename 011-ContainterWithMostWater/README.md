## Comtainer with most water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

![image-20200115204557644](/Users/msy/Library/Application Support/typora-user-images/image-20200115204557644.png)

### Solution

Two pointers：分别指在头尾，移动更新maxContainer

​	移动判断条件: 更短的那一边

​	更新判断条件: 取更大的值

