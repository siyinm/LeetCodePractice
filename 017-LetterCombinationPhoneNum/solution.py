class Solution:
    def letterCombinations_dfs(self, digits: str) -> List[str]:
        if not digits:
            return ''
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        ans = []
        temp =''

        def dfs( words,  temp):
            if not words: 
                ans.append(temp)
                return 
            for c in phone[words[0]]:
                temp += c
                dfs(words[1:], temp)
                temp=temp[:-1]
        dfs(digits, temp)
        return ans

    def letterCombinations_bfs(self, digits: str) -> List[str]:
        if not digits:
            return ''
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        ans = ['']
        for c in digits:
            letter = phone[c]
            size = len(ans)
            for _ in range(size):
                front=ans.pop(0)
                for i in letter:
                    ans.append(front+i)

        return ans