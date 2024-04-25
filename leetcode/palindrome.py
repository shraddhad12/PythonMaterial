class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if s == " " and s == "":
            return True
        s1= ''.join(letter for letter in s if letter.isalnum())
        s1 = s1.replace(" ", "").lower()
        if s1 == s1[::-1]:
            return True
        else:
            return False
        
    
s = "A man, a plan, a canal: Panama"
k = Solution().isPalindrome(s)
print(k)