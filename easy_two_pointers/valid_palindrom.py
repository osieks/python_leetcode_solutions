from math import floor
import re

class Solution:
    #beats 
    # 89% of users in runtime
    # 69% (nice) of users in memory 
    def remove_non_alphanumeric(self, s):
        return "".join(c for c in s if c.isalnum()).upper()

    def isPalindrome(self, s: str) -> bool:
        s = self.remove_non_alphanumeric(s)
        # print(s)
        middle = floor(len(s) / 2)
        # print(len(s),middle)
        if middle == 0:
            return True
        x = 0
        while x <= middle:
            # print(x)
            # print(s[x],s[(x*(-1))-1])
            if s[x] != s[(x * (-1)) - 1]:
                return False
            x += 1
        return True
        
solution = Solution()
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome( "A man, a plan, a canal: Panama"))
print(solution.isPalindrome(" "))