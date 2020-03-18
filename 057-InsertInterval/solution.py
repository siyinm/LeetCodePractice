class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        self.merge(intervals)
        return intervals
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        while i <len(intervals)-1:
            if intervals[i][1]<intervals[i+1][0]:
                i += 1
                continue 
            intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
            del intervals[i+1]
            
        return intervals
