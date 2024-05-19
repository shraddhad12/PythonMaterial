class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        s1 = s[::-1]
        for i in range(len(s1)):
            s[i] = s1[i]
        print(s)
        

s = ["h","e","l","l","o"]
Solution().reverseString(s)