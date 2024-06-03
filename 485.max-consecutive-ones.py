#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count =0
        max =0
        for val in nums:
            if val ==1:
                count +=1
            else:
                count =0
            if count>max:
                max = count


        return max
# @lc code=end

