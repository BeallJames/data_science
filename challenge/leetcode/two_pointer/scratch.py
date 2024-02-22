from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threesumlist = []
        nums.sort()
        for i in range(0, len(nums)-3):
            print('i:', i, 'nums[i]:', nums[i])
            if nums[i]>0:
                break
            if nums[i] == nums[i+1]:
                continue
            for j in range(i+2, len(nums)):
                print('j:', j, 'nums[j]:', nums[j])
                if -(nums[i]+nums[j]) in nums and (i<nums.index(-(nums[i]+nums[j]))<j):
                    threesumlist.append([nums[i], -(nums[i]+nums[j]), nums[j]])
                j += 1
            i += 1
        return threesumlist


# nums = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
nums = [-4,-2,-1,-1,0,1,2]
print(len(nums))
s = Solution()
print(s.threeSum(nums))
print(sorted(nums))