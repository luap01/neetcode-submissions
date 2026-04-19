class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 1
        r = 50000
        res = 0

        while l <= r:
            m = (l + r) // 2

            d = 1
            curr_w = 0
            # m=3
            # 1 day1
            # 
            for w in weights:
                if w > m:
                    d = days + 1
                    break
                elif curr_w + w > m:
                    d += 1
                    curr_w = w
                else:
                    curr_w += w

            if d <= days:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
                

