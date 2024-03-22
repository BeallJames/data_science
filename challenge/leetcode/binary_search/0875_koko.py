from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        for trysize in range(1, max(piles) + 1):
            time = 0
            for pile in piles:
                if pile % trysize != 0:
                    time += 1
                    # print(f"%{pile} {trysize} {pile % trysize}")
                time += pile // trysize
                # print(f"//{pile} {trysize} {pile // trysize}")
                # print(f"time {time}")
            if time <= h:
                smallestpile = trysize
                break
        return smallestpile


piles = [30, 11, 23, 4, 20]
h = 5

sol = Solution()
print(sol.minEatingSpeed(piles, h))
