Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.


### Solution
贪心算法，每一步计算能到达的最远距离，最后的大于list长度就判断为真。
