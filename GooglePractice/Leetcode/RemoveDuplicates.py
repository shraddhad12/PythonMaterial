# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         length = len(nums)
        
#         k = len(nums)
#         placeholder = (length - k) * "_"
#         nums =  (list(nums)) + (list(placeholder))
#         return k
    
# print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
k = Solution().removeDuplicates(nums)
print(k)
    



