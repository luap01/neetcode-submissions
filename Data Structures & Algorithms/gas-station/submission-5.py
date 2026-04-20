class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        total = 0
        idx = 0
        sum_all = 0
        for i in range(len(gas)):
            sum_all += (gas[i] - cost[i])
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                idx = i + 1
        
        return idx if sum_all >= 0 else -1
