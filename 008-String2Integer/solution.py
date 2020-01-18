import re
class Solution:
    def myAtoi(self, str: str) -> int:
        string = re.findall('^\s*([-+]?[0-9]+)',str)
        if not string: 
            return 0
        number = int(string[0])
        if number < -2**31:
            return -2**31
        if number > 2**31-1:
            return 2**31-1
        return number

