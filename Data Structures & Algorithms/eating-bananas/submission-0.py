class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 1
        while l <= r:
            k = (l + r) // 2
            hr = 0
            for i in piles:
                hr += math.ceil(i / k)
            
            if hr <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1
        
        return ans
