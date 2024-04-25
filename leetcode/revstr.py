class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s[::k]
        return s
    
s = "abcdefg"
k = 2
k = Solution().reverseStr(s, k)
print(k)