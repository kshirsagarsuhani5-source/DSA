class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {}
        
        for i, ch in enumerate(s):
            last[ch] = i
        
        stack = []
        seen = set()
        
        for i, ch in enumerate(s):
            
            # If character is already present, skip it
            if ch in seen:
                continue
            
            # Remove larger characters if they occur again later
            while (stack and
                   stack[-1] > ch and
                   last[stack[-1]] > i):
                
                removed = stack.pop()
                seen.remove(removed)
            
            stack.append(ch)
            seen.add(ch)
        
        return ''.join(stack)  