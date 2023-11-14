# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest: # T: 17.69% M: 17.30%
    def __init__(self, k: int, nums: list[int]):
        self.arr = []
        self.max_ln = k
        for n in nums:
            self.add(n)
        
    def add(self, val: int) -> int:
        if len(self.arr) < self.max_ln: # If array isn't full 
            self.arr.append(val)
            index = len(self.arr) - 1
            
            while index > 0:
                parent_id = (index - 1) // 2
                parent = self.arr[parent_id]
                if parent > val:
                    self.arr[index] = parent
                    self.arr[parent_id] = val
                    index = parent_id
                else:
                    break
                
        elif val > self.arr[0]: # If array is full
            self.arr[0] = val
            index = 0
            while True:
                l_id = (index * 2) + 1
                l_child = self.arr[l_id] if l_id < self.max_ln else float('inf')
                r_id = (index * 2) + 2
                r_child = self.arr[r_id] if r_id < self.max_ln else float('inf')
                
                if val > l_child or val > r_child:
                    if r_child < l_child:
                        self.arr[index] = r_child
                        self.arr[r_id] = val
                        index = r_id
                    else:
                        self.arr[index] = l_child
                        self.arr[l_id] = val
                        index = l_id
                else:
                    break
                
        return self.arr[0]

import heapq

class KthLargest: # T: 70.57% M: 65.52%
    #@ https://www.youtube.com/watch?v=hOjcdrqMoQ8
    def __init__(self, k: int, nums: list[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
