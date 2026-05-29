class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
     
        queue = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        completed = 0
        
        while queue:
            
            current = queue.popleft()
            completed += 1
            
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return completed == numCourses