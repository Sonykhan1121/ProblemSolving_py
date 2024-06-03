#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        find = n
        for i in range(n):
            find+=(i-nums[i])
        return find
        
        
# @lc code=end

if __name__ == '__main__':
    now = Solution()
    print(now.missingNumber([2,0]))