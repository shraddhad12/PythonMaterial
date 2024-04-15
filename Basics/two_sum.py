
class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        sum=[]
        dict={}
        for i in range(len(nums)):
            remaining=target-nums[i]
            if remaining in dict:
                index=dict[remaining]
                return [index, i]
            dict[nums[i]]=i
            print(dict)


nums=[4,8, 6, 5,7,8]
target=9
sum = Solution().twoSum(nums, target)
print(sum)