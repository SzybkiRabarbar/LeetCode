# https://leetcode.com/problems/task-scheduler/

from collections import Counter, deque
import heapq

class Solution: # T: 67.60% M: 16.64%
    #@https://www.youtube.com/watch?v=s8p8ukTyA2I
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

# Greedy algorithm
from collections import Counter

class Solution: # T: 98.98% M: 16.64%
    #@https://www.youtube.com/watch?v=s8p8ukTyA2I
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        max_count = max(counter.values())
        min_time = (max_count - 1) * (n + 1) + \
                    sum(map(lambda count: count == max_count, counter.values()))
    
        return max(min_time, len(tasks))