class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        courses = [[] for i in range(numCourses)]
        for course, prereq in prerequisites:
            indegree[course] += 1
            courses[prereq].append(course)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        done = 0
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            done += 1
            for neighbor in courses[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if done != numCourses:
            return []
        return result
        
        
