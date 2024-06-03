#
# @lc app=leetcode id=1838 lang=python3
#
# [1838] Frequency of the Most Frequent Element
#

# @lc code=start



class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        pre = [0]*n
        ans =1
        # for i in range(0,n):
        #     if i==0:
        #         pre[i] = nums[i]
        #     else:
        #         pre[i] = pre[i-1] + nums[i]
        # print(*pre)
        left = 0
        total_have = 0
        for i in range(n):
            
            total_have += nums[i]
            total_needed= nums[i]*(i-left+1)
            if total_have +k>= total_needed:
                ans = max(ans,i-left+1)
            else:
                while left <  i and total_have+k < total_needed:
                    total_have-=nums[left]
                    left+=1
                    total_needed-=nums[i]
                ans = max(ans,i-left+1)



        return ans

# @lc code=end

if __name__ == '__main__':
    now = Solution()
    print(now.maxFrequency([1,2,4],5))