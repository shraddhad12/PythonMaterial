class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m != len(nums1):
            nums1.pop()

        res = nums1
        if m == len(nums1) and n == len(nums2):
            for i in nums2:
                nums1.append(i) 
            print(nums1)
            if m+n == len(nums1):
                nums1.sort()
                print(nums1)
        

nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,3]
m=6
n=3
Solution().merge(nums1, m, nums2, n)