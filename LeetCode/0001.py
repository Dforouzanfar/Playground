# URL: https://leetcode.com/problems/two-sum/
 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map_dict = {}

        for i, num in enumerate(nums):
            x = target - num
            if x in map_dict:
                return [map_dict[x], i]
            map_dict[num] = i