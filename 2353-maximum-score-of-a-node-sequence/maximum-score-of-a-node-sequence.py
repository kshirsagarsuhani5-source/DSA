class Solution(object):
    def maximumScore(self, scores, edges):
        """
        :type scores: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(scores)
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Keep only the best 3 neighbors of each node
        for i in range(n):
            graph[i].sort(key=lambda x: scores[x], reverse=True)
            graph[i] = graph[i][:3]

        ans = -1

        for a, b in edges:
            for c in graph[a]:
                if c == b:
                    continue

                for d in graph[b]:
                    if d == a or d == c:
                        continue

                    total = scores[c] + scores[a] + scores[b] + scores[d]
                    ans = max(ans, total)

        return ans