class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        for i in digits:
            s = s + str(i)
        s = int(s) + 1
        print(s)
        res = [int(x) for x in str(s)]
        return res
        
nums = [1,2,9,9]
k = Solution().plusOne(nums)
print(k)