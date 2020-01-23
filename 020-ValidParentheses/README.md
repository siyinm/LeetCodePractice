## Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

### Solution:

Stack:

左括号入栈，右括号与栈顶匹配，若匹配则栈顶pop，若不匹配则返回错误

