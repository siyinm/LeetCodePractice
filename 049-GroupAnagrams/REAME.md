Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
### Solution
hash map 不同的实现方式：
1. 用pythond的dic{}，使用sort原字符串使异位词变得一样。
2. 用质数表达每个字母，乘积相同的放到一起
