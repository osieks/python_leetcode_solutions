class Solution:
    # 38 ms, 16 MB
    # beats:
    # 55% in runtime
    # 66% in memory
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        elif len(t)==0:
            return False
        y=0
        for x in range(0,len(t)):
            print(t[x],s[y])
            if t[x]==s[y]:
                y+=1
                if y>=len(s):
                    return True
        return False
        
sol=Solution()        
print(sol.isSubsequence("abc","ahbgdc"))
print(sol.isSubsequence("axc","ahbgdc"))
print(sol.isSubsequence("","ahbgdc"))