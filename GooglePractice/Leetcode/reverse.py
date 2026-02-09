class Solution:

    def reverse(self, x):
        if x < 0:
            x = abs(x)
            result = str(x)[::-1]
            return -abs(int(result))
        else:
            result = str(x)[::-1]
            return abs(int(result))


result = Solution().reverse(-321)
print(result)


