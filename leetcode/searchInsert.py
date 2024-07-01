class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target <= nums[i]:
                nums.insert(i, target)
                return i, nums
        else:
            if nums[i] >= target:
                nums.insert(i-1, target)
                return i-1, nums
            elif nums[i] < target:
                nums.insert(i+1, target)
                return i+1, nums

        
nums = [1,3,5,6]
target = 4
print(Solution().searchInsert(nums, target))