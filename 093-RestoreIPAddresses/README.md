Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

```
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
```

### Solution

回溯法：

限制条件有：

一共四个dots, 每个字符数字在0-255之间，以0开头只能单独分组

- 先总长度筛选 >12去除
- 在回溯过程中分为三部：
  - 加一位 （都可以）
  - 加两位 （第一位不是0）
  - 加三位 （第一位不是0， 0-255）