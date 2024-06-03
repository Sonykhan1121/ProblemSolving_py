#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        i =j=0
        
        while i<n:
            nums[j] = nums[i]
            
            while i+1<n and nums[i+1] == nums[j]:
                i+=1
            
            i+=1
            j+=1
        return j
# @lc code=end

