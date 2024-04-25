class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        xor =0 
        for num in nums:
            xor ^= num #[4+1+2-1-1+2]
            print(xor)
        
        return xor
        

nums = [4,1,2,1,2]
k = Solution().singleNumber(nums)
