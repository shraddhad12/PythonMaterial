class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip().split(" ")
        last_word = s[::-1][0]
        print(last_word)
        return len(last_word)
    
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        
        if not words:
            return 0
        
        return len(words[-1])

s = "   fly me   to   the moon  "
l = Solution().lengthOfLastWord(s)
print(l)