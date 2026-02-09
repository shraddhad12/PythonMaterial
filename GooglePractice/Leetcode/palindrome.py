class Solution:

    def palindrome(self, num):
        return True if str(num) == str(num)[::-1] else False
            
        
print(Solution().palindrome(-121))