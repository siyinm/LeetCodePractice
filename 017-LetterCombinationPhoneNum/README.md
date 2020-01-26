## [Letter Combinations of a Phone Number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![img](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

Example:

```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

### Solution

#### DFS 深度优先

recursion: 从最底层开始

```def dfs( words,  temp):```

words变量为当前数字组合，本轮处理words[0], 用temp变量存下当前字母组合

递归结束条件：words为空

递归内部循环中调用递归：调用递归之后记得把dfs最后一位删掉

#### BFS 广度优先

queue：FIFO 

依次取出queue中元素，拼接当前数字的每一个对应字母，再依次放回queue

大循环次数len(digits): 每一层

中间循环次数len(queue): 每一个queue中元素

小循环次数len(phone(c)): 当前数字的每一个对应字母