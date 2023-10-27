# https://leetcode.com/problems/car-fleet/

class Solution: # T: 92.22% M: 22.41%
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        road = sorted(zip(position, speed),key=lambda x: x[0]) #| could be done with storing sorted index (lower memory usage)
        result = 1
        head = ()
        while road:
            tail = road.pop()
            if not head:
                head = tail
            elif head[1] >= tail[1] or ((target - head[0]) / head[1]) < ((target - tail[0]) / tail[1]):
                result += 1
                head = tail
        return result
                    
if __name__=="__main__":
    s = Solution()
    print(s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))