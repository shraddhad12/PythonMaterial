class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     n = list(set(nums))
    #     print(n)
    #     k = len(n)
    #     return k

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        list=[]
        for i in range(len(nums)):
            if nums[i] not in list:
                list.append(nums[i])
        print(list)
        return len(list)

nums = [1,1,2]
k = Solution().removeDuplicates(nums)
print(k)



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
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
k = Solution().removeDuplicates(nums)