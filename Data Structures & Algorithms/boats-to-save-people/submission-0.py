class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 1 2 4 5

        # 5+1 = 6
        # 4+2 = 6


        # 1 2 2 3 3
        # 1 1 1 1 3 3 3 4


        # 1 + 3 > limit +1
        # 1 + 3 > limit +1
        people = sorted(people)
        l = 0
        r = len(people) - 1
        res = 0

        # 1 2 4 5
        # 1 + 5 = 6
        # 6 + 2 + 4 = 12
        
        # 1 2 2 3 3 
        # 1       3
        # 
        # 3
        # 3
        # 1 + 2 = 3
        # 
        while l < r:
            curr = people[l] + people[r]
            l += 1
            r -= 1
            while curr + people[l] + people[r] < limit and l < r:
                curr += people[l] + people[r]
                l += 1
                r -= 1

            if curr > limit and curr - people[l] <= limit:
                l -= 1
            elif curr > limit and curr - people[r] <= limit:
                r += 1
                while curr + people[l] < limit and l < r:
                    curr += people[l]
                    l += 1
            
            if l == r:
                res += 1
                
            res += 1
        
    

        return res