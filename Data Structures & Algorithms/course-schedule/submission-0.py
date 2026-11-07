class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Step 1: Create an adjacency list
        prereq = {}

        for course in range(numCourses):
            prereq[course] = []

        for course, pre in prerequisites:
            prereq[course].append(pre)

        # Step 2: Track courses in the current DFS path
        visiting = set()

        def dfs(course):

            # Cycle detected
            if course in visiting:
                return False

            # No remaining prerequisites
            if prereq[course] == []:
                return True

            # Mark current course as being explored
            visiting.add(course)

            # Explore its prerequisites
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False

            # Finished exploring this course
            visiting.remove(course)

            # Mark this course as completed
            prereq[course] = []

            return True

        # Step 3: Check every course
        for course in range(numCourses):
            if dfs(course) == False:
                return False

        return True