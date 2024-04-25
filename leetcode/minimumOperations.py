class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = nums.sort()
    
        
        
nums = [4,1,2,1,2]
k = Solution().singleNumber(nums)
print(k)