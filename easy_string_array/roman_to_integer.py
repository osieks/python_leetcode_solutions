class Solution:
    TABLE_ROMAN = [
    ["I",1],
    ["V",5],
    ["X",10],
    ["L",50],
    ["C",100],
    ["D",500],
    ["M",1000]
    ]
    def romanToInt(self, s: str) -> int:
        wynik = 0
        prev_val=0
        for x in range(len(s)):
            i=0
            while s[x] != self.TABLE_ROMAN[i][0]:
                #print("letter:",s[x]," != ","table[i][0]:",table[i][0])
                i+=1
            if s[x] == self.TABLE_ROMAN[i][0]:
                #print("letter:",s[x]," == ","table[i][0]:",table[i][0]) 
                if prev_val<self.TABLE_ROMAN[i][1]:
                    wynik-=2*prev_val  
                #print(wynik,"+",table[i][1])
                wynik += self.TABLE_ROMAN[i][1]
                #print(wynik) 
                prev_val=self.TABLE_ROMAN[i][1]
        #print(wynik)
        return wynik
    
    MAP_ROMAN = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    def roman_to_int_with_map(self,s:str) -> int:
        wynik = 0

        for x in range(len(s)):
            if x<(len(s)-1) and self.MAP_ROMAN[s[x]]<self.MAP_ROMAN[s[x+1]]:
                wynik -= self.MAP_ROMAN[s[x]]
            else:
                wynik += self.MAP_ROMAN[s[x]]
        return wynik
    
solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))
print(solution.roman_to_int_with_map("III"))
print(solution.roman_to_int_with_map("LVIII"))
print(solution.roman_to_int_with_map("MCMXCIV"))