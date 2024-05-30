
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
                print(index, i , "of numbers", nums[index], nums[i])
            dict[nums[i]]=i

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if i == j:
                    print(i, j, "same")
                    continue
                elif nums[i] + nums[j] == target:
                    print(i, j , "of numbers", nums[i], nums[j] )
                    continue
                 
        


nums=[4,8,6,1, 5,7,8]
target=9

Solution().twoSum(nums, target)
print("=======================================")

nums=[4,8,6,1, 5,7,8]
target=9
Solution().twoSum2(nums, target)