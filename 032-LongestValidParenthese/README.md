Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

### Solution

stack+dynamic programming

Loop 1: 

使用stack判断valid组合，若为左括号将index入栈

若为右括号则pop，每次pop的时候，通过一个数组储存 "(" ")" 两个位置，记录为1

Loop 2: 再通过一个循环处理储存valid的数组，1则累加，0则清零，判断最大值