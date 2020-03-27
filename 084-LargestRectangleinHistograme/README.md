Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

### Solution

单调栈

单调栈分为单调递增栈和单调递减栈
11. 单调递增栈即栈内元素保持单调递增的栈
12. 同理单调递减栈即栈内元素保持单调递减的栈

操作规则（下面都以单调递增栈为例）
21. 如果新的元素比栈顶元素大，就入栈
22. 如果新的元素较小，那就一直把栈内元素弹出来，直到栈顶比新元素小

加入这样一个规则之后，会有什么效果
31. 栈内的元素是递增的
32. 当元素出栈时，说明这个新元素是出栈元素向后找第一个比其小的元素

The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the building who is taller than the new one. The building popped out represent the height of a rectangle with the new building as the right boundary and the current stack top as the left boundary. Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.