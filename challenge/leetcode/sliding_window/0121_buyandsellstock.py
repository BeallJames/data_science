from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return len(prices)


prices = [7, 1, 5, 3, 6, 4]
# output = 5

sol = Solution()
print(sol.maxProfit(prices))
