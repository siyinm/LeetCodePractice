## Roman to Integer

Example 5:

```{}
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```



### Solution

- Hash Map: find the number corresponding to the roman character.

- Consider two conditions —— one or two characters, at the same time：如果某个单个罗马字符```c```右边单字符代表队数字比```c```本身大, 表示这是个两位字符。

