class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #build the adjency list 
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a,b in prerequisites:
            adjList[b].append(a) #b -> a
            indegree[a] += 1
        
        q = deque()

        for course in range(numCourses):

            if indegree[course] == 0:
                q.append(course)
        
        taken = 0

        while q:
            course = q.popleft()
            taken += 1

            for dependant in adjList[course]:
                indegree[dependant] -= 1
                if indegree[dependant] == 0:
                    q.append(dependant)
        
        return taken == numCourses
        
        
        


            


