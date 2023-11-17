# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder: # T: 18.23% M: 69.62%
    def __init__(self):
        self.top_heap = []
        self.mid = False
        self.bottom_heap = []
    
    def addNum(self, num: int) -> None:
        if not isinstance(self.mid, bool):
            if not self.top_heap and not self.bottom_heap:
                if self.mid > num:
                    heapq.heappush(self.top_heap, self.mid)
                    heapq.heappush(self.bottom_heap, - num)
                else:
                    heapq.heappush(self.top_heap, num)
                    heapq.heappush(self.bottom_heap, - self.mid)
            else:
                top = heapq.heappop(self.top_heap)
                bot = - heapq.heappop(self.bottom_heap)
                res = sorted([bot, self.mid, num, top])
                for n in res[:2]:
                    heapq.heappush(self.bottom_heap, - n)
                for n in res[2:]:
                    heapq.heappush(self.top_heap, n)
            self.mid = False
        else:
            if not self.top_heap and not self.bottom_heap:
                self.mid = num
            else:
                top = heapq.heappop(self.top_heap)
                bot = - heapq.heappop(self.bottom_heap)
                res = sorted([bot, num, top])
                
                heapq.heappush(self.top_heap, res[2])
                self.mid = res[1]
                heapq.heappush(self.bottom_heap, - res[0])
        
    def findMedian(self) -> float:
        if not isinstance(self.mid, bool):
            return self.mid
        else:
            return (self.top_heap[0] + (self.bottom_heap[0] * -1)) / 2 
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

