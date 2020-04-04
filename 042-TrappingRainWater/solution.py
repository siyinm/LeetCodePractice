class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<=2: return 0
        m = max(height)
        n = len(height)
        s = sum(height)
        mindex = height.index(m)
        lmax = height[0]
        rmax = height[n-1]
        rain = 0
        
        for i in range(0, mindex):
            lmax = max(lmax, height[i])
            rain += lmax
        
        for j in range(n-1, mindex, -1):
            rmax = max(rmax, height[j])
            rain += rmax
        
            
        return rain-s+m
