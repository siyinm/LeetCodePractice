
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = int(num1)
        res = 0
        bit = 1

        for num in reversed(num2):
            res += int(num) * a * bit
            bit *= 10
        return str(res)
