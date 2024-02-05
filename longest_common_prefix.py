from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(len(strs))
        common_letters=""
        str_num=len(strs)
        for x in range(0,len(strs[0])):
            for y in range(1,len(strs)): 
                try:
                    if strs[0][x]!=strs[y][x]:
                        return common_letters
                except:
                    return common_letters
            common_letters+=strs[0][x]
        return common_letters
        
solution = Solution()
print(solution.longestCommonPrefix(["dog","racecar","car"]))
print(solution.longestCommonPrefix(["flower","flow","flight"]))