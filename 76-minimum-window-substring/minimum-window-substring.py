from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        need = Counter(t)
        window = {}

        have=0
        need_count=len(need)

        left=0
        result=[-1,-1]
        result_len = float("inf")

        for right in range(len(s)):
            
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                have += 1
            while have == need_count:
                
                if (right - left + 1) < result_len:
                    result = [left, right]
                    result_len = right - left + 1
                
                window[s[left]] -= 1
                
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                
                left += 1
        left, right = result
        
        return s[left:right + 1] if result_len != float("inf") else ""





