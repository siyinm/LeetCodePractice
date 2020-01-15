## Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

### Solution

- Greedy algorithm: 类似找钱，永远先用面值最大的
- 先列出所有可能性，可以用hash map

- 注意400，500，900这种4 5 9为并列关系