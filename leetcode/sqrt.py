class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sqrt = x**0.5
        return int(sqrt)
        
num = 16
sqrt = Solution().mySqrt(num)
print(sqrt)