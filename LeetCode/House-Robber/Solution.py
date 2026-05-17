1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        # Base cases for 1 or 2 houses
6        if n == 1:
7            return nums[0]
8        if n == 2:
9            return max(nums[0], nums[1])
10
11        # result[i] stores the max money robbed up to house i
12        result = [0] * (n + 1)
13
14        result[0] = nums[0]
15        result[1] = max(nums[0], nums[1])
16
17        for i in range(2, n):
18            # Option 1: Rob this house (nums[i]) and add profit from i-2
19            steal = nums[i] + result[i - 2]
20            # Option 2: Skip this house and take profit from i-1
21            skip = result[i - 1]
22
23            result[i] = max(steal, skip)
24
25        return result[n-1]