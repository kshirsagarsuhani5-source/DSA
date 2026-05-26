class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        
        if not s:
            return 0
        
        sign = 1
        index = 0
        result = 0
        
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        result *= sign
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        
        if result > INT_MAX:
            return INT_MAX
        
        return result