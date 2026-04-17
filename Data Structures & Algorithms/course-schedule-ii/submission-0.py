class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            adjList[b].append(a)
            indegree[a] += 1
        
        q = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        result = []
        while q:
            course = q.popleft()
            result.append(course)

            for neighbour in adjList[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)

        if len(result) == numCourses:
            return result
        else:
            return []