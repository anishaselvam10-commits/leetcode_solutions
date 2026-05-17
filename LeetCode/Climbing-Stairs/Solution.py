1class Solution:
2    def climbStairs(self, n: int, memo = {}) -> int:
3        if n == 0 or n == 1: 
4            return 1
5        if n in memo: 
6            return memo[n]
7        memo[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
8        return memo[n]