class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)-1
        len_needle = len(needle)-1
        if len_needle>len_haystack:
            return -1
        y=0
        x=0
        try:
            while x<(len_haystack+1):
                if haystack[x]!=needle[y]:
                    x-=y-1
                    y=0
                    skip=0
                if haystack[x]==needle[y]:
                    if y==len_needle:
                        return x-y
                    y+=1
                    print("haystack",haystack[x])
                x+=1
        except:
            return -1
        return -1
            

solution = Solution()
print(solution.strStr("aabaaabaaac","aabaaac"))
print(solution.strStr("mississippi","pi"))
print(solution.strStr("aaaaa","bba"))
print(solution.strStr("mississippi","issip"))
print(solution.strStr("a","a"))
print(solution.strStr("sadbutsad","sad"))
print(solution.strStr("leetcode","leeto"))