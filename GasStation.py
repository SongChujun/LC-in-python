class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        sum = 0
        min = float('inf')
        p = -1
        for i in range(length):
            sum += gas[i]-cost[i]
            if sum < min:
                min = sum
                p = i
        if sum < 0:
            return -1
        else:
            return (p + 1) % length