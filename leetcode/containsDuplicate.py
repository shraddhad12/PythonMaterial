class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if 1 <= len(nums) <= 10**5 and -10**9 <= sorted(nums)[-1] <= 10**9:
            unique = list(set(nums))
            if len(nums) != len(unique):
                return True
            else:
                return False
        else:
            return False
             
        

nums = [4,1,2,2]
k = Solution().containsDuplicate(nums)
print(k)
