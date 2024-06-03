#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def r(self,nums,left,right):
        while left<right:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
            right-=1
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k%=n
        nums.reverse()
        self.r(nums,0,k-1)
        self.r(nums,k,n-1)
        return nums
        
# @lc code=end

# if __name__ == '__main__':
#     now = Solution()
#     print(now.rotate([1,2,3,4,5,6,7],3))