class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # for i in s.split(" "):
        #     if i == "":
        #         continue
        #     if "-" in i:
        #         i = i.replace("-", "")
        #         if i.isdigit():
        #             if -abs(int(i)) > pow(-2,31):
        #                 return -abs(int(i))
        #             return -abs(pow(-2,31))
        #         else:
        #             return 0
        #     elif i.isdigit():
        #         if int(i) > (pow(2,31) - 1):
        #             return pow(-2,31)
        #         else:
        #             return int(i)
        #     else:
        #         return 0

        number = 0
        counter = 0
        isNegative = False
        s= s.strip()
        if s == "":
            return 0
        if s[0] == "-":
            isNegative = True
            s = s[1:]
            if s[0] == "+":
                return 0
        for i in s:
            if i == "." or i.isalpha() or not i.isdigit():
                break
            if i.isdigit():
                number = counter + int(i)
                counter = 10 * number
        number = -abs(number) if isNegative else number
        if number < pow(-2,31):
            return -abs(pow(-2,31))
        return number

s="+12"
result=Solution().myAtoi(s)
print(result)