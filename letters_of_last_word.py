class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        x = len(s) - 1
        while s[x] != " " or length == 0:
            if s[x] != " ":
                length += 1
            x -= 1
            if x<0:
                break

        return length

solution = Solution()
print(solution.lengthOfLastWord("Hello world"))
print(solution.lengthOfLastWord(" "))
print(solution.lengthOfLastWord("a"))
print(solution.lengthOfLastWord("Why    "))