class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # Step 1: Build the prerequisite dictionary
        prereq = {}

        for course in range(numCourses):
            prereq[course] = []

        for course, pre in prerequisites:
            prereq[course].append(pre)

        # Step 2: Initialize variables
        visiting = set()
        visited = set()
        result = []

        # Step 3: DFS
        def dfs(course):

            # Cycle detected
            if course in visiting:
                return False

            # Already checked this course
            if course in visited:
                return True

            # Add course to current DFS path
            visiting.add(course)

            # Check all prerequisites
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False

            # Finished checking this course
            visiting.remove(course)
            visited.add(course)

            # Add course to result
            result.append(course)

            return True

        # Step 4: Check every course
        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return result