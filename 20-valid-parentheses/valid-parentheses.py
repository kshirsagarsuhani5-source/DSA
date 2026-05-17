class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        mapping={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if char in mapping.values():
                stack.append(char)

            elif char in mapping.keys():
                if stack==[] or mapping[char]!=stack.pop():
                    return False
            else:
                return False
                
        return stack==[]