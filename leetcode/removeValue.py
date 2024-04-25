class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # l =[]
        # for i in range(len(nums)-1):
        #     if nums[i] == val:
        #         continue
        #     else:
        #         l.append(nums[i])
        # return len(l)
        while val in nums:
            nums.remove(val)
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,3,3,4]
print(len(nums))
k = Solution().removeElement(nums, 3)
print(k)