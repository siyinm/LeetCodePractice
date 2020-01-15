 ## Paralindrom number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

```{}
Example 1:

Input: 121
Output: true

```

### Solution

```{python}
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
```



