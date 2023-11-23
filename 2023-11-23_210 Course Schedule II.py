# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict

class Solution: # T: 77.03% M: 7.77%
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        hash_req = defaultdict(list)
        for course, req in prerequisites:
            hash_req[course].append(req)
        result = []
        in_res = set()
        
        def func(num: int, seen: set) -> bool:
            if num in in_res: return False
            if num in seen: return True
            seen.add(num)
            for next_ in hash_req[num]:
                if func(next_, seen):
                    return True
            result.append(num)
            in_res.add(num)
            return False
        
        for num in range(numCourses):
            seen = set()
            if func(num, seen):
                return []
        return result
        
            
                
                
                