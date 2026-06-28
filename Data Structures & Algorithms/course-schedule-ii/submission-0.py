

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # construct graph
        # adjacency list + indegree list to keep track of how many dependencies a node has
            # indegree[nodes] = num of dependencies a node has
            # ex. indegree[2] = 4, course 2 has 4 prerequisites

        indegree = [0] * numCourses
        adj_list = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            indegree[course] += 1  
            adj_list[prereq].append(course)

       # iterative dfs       

        q = deque()

       # add all independent courses first

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        processed = 0
        ret = []

        while q:
            curr = q.popleft()
            ret.append(curr)
            processed += 1

            for neighbor in adj_list[curr]:
                # this course has been processed so other courses are not blocked by this course anymore
                # we need to reduce indegree by 1 since this course is gone and all other courses are not dependent on it anymore

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    # all prereqs for a course have been cleared so now we can take this course
                    q.append(neighbor)
                
        if processed == numCourses:
            return ret
        else: return [] # cycle dependency. if cycle exists, indegree never becomes 0 so q is empty and e do not process all the courses

