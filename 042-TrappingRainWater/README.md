## Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![image-20200118152730480](/Users/msy/Library/Application Support/typora-user-images/image-20200118152730480.png)

### Solution

1. Stack:
   - use a stack to store the axis (0,1,2...)
   - pop if the current height > stack.top( )
   - calculate the rain in that block( the popped top) add to the answer
   - notice: empty stack
2. Two pointers:
   - one pointer from right to left, one seek for the heightest block/heigher than right pointer
   - calculate the rain inside the two pointers
   - let right=left and left--