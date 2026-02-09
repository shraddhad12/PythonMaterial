import array

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums = array.array('i', nums)
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop()
        print(array)

Solution().rotate([1,2,3,4,5,6,7], k = 3)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k > n 
        # Reverse the entire array
        nums.reverse()
        # Reverse first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse the rest
        nums[k:] = reversed(nums[k:])

Solution().rotate([1,2,3,4,5,6,7,6,9], k = 3)