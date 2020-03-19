Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example `"Aa"` is not considered a palindrome here.

**Note:**
Assume the length of given string will not exceed 1,010.

### Solution:

- use dict() in python to construct hash table
- for every value in the dict(), when even, add all; when odd, add num-1
- After the loop, if there is at least one odd number, sum+=1