#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        now =0
        for val in nums:
            now^=val


        return now
# @lc code=end

