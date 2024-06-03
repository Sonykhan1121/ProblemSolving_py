#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        j=0
        for i in range(n):
            if nums[i] !=0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1
        
# @lc code=end

