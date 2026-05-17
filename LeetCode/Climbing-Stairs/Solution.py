class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n == 0 or n == 1: 
            return 1
        if n in memo: 
            return memo[n]
        memo[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return memo[n]