from collections import Counter, defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hashmap = defaultdict(int)
        for x in magazine:
            magazine_hashmap[x]+=1
        
        for y in ransomNote:
            if magazine_hashmap[y]>0:
                magazine_hashmap[y]-=1
            else:
                return False
            
        return True
    
    def canConstruct2(self, ransomNote, magazine):
        #from solutions
            st1, st2 = Counter(ransomNote), Counter(magazine)
            return st1 & st2 == st1
        
    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        a = set(ransomNote) 
        for i in a:
            if magazine.count(i)<ransomNote.count(i):
              return False
        return True
solution = Solution()
print(solution.canConstruct3("a","b"))
print(solution.canConstruct3("aa","ab"))
print(solution.canConstruct3("aa","aab"))