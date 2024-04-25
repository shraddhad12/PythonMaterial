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

s = "   fly me   to   the moon  "
l = Solution().lengthOfLastWord(s)
print(l)