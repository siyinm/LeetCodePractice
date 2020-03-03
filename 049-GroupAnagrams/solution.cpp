class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        res = []
        for s in strs:
            keys = "".join(sorted(s))
            if keys not in dic:
                dic[keys] = [s];
            else:
                dic[keys].append(s)
        return list(dic.values())
