#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)

        count=0
        for i in range(n):
            if(nums[i]>nums[(i+1)%n]):
                count +=1
                
                
        



        return True if count <=1 else False
        
# @lc code=end

