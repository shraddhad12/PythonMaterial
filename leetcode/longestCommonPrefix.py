class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if 1 <= len(strs) <= 200:
            longest_prefix = ''
            for i in range(len(sorted(strs, key=len)[0])):
                longest_prefix += strs[i][0]
                for j in range(len(strs)):
                    if strs[i][j] == longest_prefix:
                        
                        print(longest_prefix)

            
            return longest_prefix
        else:
            return ""
        

strs = ["flow", "flight", "flo"]
print(Solution().longestCommonPrefix(strs))