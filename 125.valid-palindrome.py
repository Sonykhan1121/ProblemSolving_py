#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = ''.join(filter(lambda x:x.isalpha() or x.isdigit(),s))
        s3 = s2[::-1]
        print(s2)
        print(s3)
        return s3==s2

# @lc code=end

if __name__ == '__main__':
    now = Solution()
    print(now.isPalindrome("0p"))
   