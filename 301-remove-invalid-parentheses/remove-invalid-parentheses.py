class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(string):
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    if count == 0:
                        return False
                    count -= 1
            return count == 0

        queue = deque([s])
        visited = set([s])
        result = []
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                result.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue

                nxt = curr[:i] + curr[i + 1:]

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result
        