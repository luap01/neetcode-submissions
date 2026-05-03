class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l = 0
        r = len(people) - 1
        res = 0
        while l < r:
            curr = people[l] + people[r]
            l += 1
            r -= 1
            if curr > limit and curr - people[l] <= limit:
                l -= 1
            elif curr > limit and curr - people[r] <= limit:
                r += 1

            res += 1
        
        if l == r:
            res += 1
    

        return res