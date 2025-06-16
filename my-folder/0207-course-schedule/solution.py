class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Topological sort (Kahn's algorithm)
        indegree = [0] * numCourses
        courses = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course] += 1
            courses[prereq].append(course)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        done = 0
        while q:
            node = q.popleft()
            done += 1
            for nei in courses[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return done == numCourses

# Time complexity = O(V+E)
# Space complexity = O(V+E)
