class Solution(object):
    # def __init__(self):
    #         self.list = []

    # def __str__(self):
    #     v = [str(i) for i in range(self.list)]
    #     return "/n".join(v)
    
    # def push(self, s):
    #         self.list.append(s)

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, c in enumerate(s):
            if s.count(c) == 1:
                return i
        return -1
          

a = "eetcode"
print(Solution().firstUniqChar(a))