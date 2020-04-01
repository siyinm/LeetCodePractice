The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:

```
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
```

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

```
00 - 0
10 - 2
11 - 3
01 - 1
```

### Solution

![pic089](http://github.com/siyinm/LeetCodePractice/raw/master/pics/pic089.png)

从最简单n=0的时候作为起点出发不断给ans增加元素，第m次迭代增加的元素无非是对二进制第m位的0改为1，那也就是原来的每个元素加上2^(m-1)便得到了，

要注意，每一次迭代都要把顺序倒一遍