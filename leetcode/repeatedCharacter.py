class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(i for i in s)
        if l[0] == l[-1]:
            return l[0]
        for i in range(len(l)-1):
            if l[i] == l[i+1]:
                return l[i]
            else:
                continue
        return ""


s = "nwcn"
k = Solution().repeatedCharacter(s)
print(k)