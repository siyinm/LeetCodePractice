## Generate Parenthese

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

![image](http://github.com/siyinm/LeetCodePractice/raw/master/022-GenerateParenthese/mindmap022.png)

### Solution

1. dfs

   建立树型结构图，剪枝

   ```left```: initially n, represent the number of "(" left

   ```right```: initailly 0, represent the number of ")"  unused

   - end: ```left=right=0```
   - add "("(left—, right++): ```left>0```
   - add")"(right—): ```right>0```  

   

2. bfs

   广度优先遍历，得程序员自己编写结点类，显示使用队列这个数据结构。深度优先遍历的时候，就可以直接使用系统栈，在递归方法执行完成的时候，系统栈顶就把我们所需要的状态信息直接弹出，而无须编写结点类和显示使用栈。

3. 动态规划：[参考](https://leetcode-cn.com/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/)

   ```python
   dp[i] = "(" + dp[可能的括号对数] + ")" + dp[剩下的括号对数]
   ```

   枚举的方式就是枚举左括号 "(" 和右括号 ")" 中间可能的合法的括号对数，而剩下的合法的括号对数在与第一个左括号 "(" 配对的右括号 ")" 的后面，这就用到了以前的状态。

   ```python
   dp[i] = "(" + dp[j] + ")" + dp[i- j - 1] , j = 0, 1, ..., i - 1
   ```

   - 初始状态：因为我们需要 `0` 对括号这种状态，因此状态数组 `dp` 从 `0` 开始，`0` 个括号当然就是 `[""]`。
   - 输出：`dp[n]` 。

