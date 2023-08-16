# https://leetcode.com/problems/trapping-rain-water/

class Solution: # T: 5% M: 21.49%
    def trap(self, height: list[int]) -> int:
        max_val_id = height.index(max(height))
        return self.left_trap(height[:max_val_id + 1]) + self.right_trap(height[max_val_id:])
    
    def left_trap(self, height: list[int]) -> int:
        dog_water = 0
        while len(height) > 1:
            id = height.index(max(height[:-1]))
            spread = len(height) - 2 - id
            dog_water += height[id] * spread - sum(height[id + 1:-1])
            height = height[:id + 1]
        return dog_water
    
    def right_trap(self, height: list[int]) -> int:
        dog_water = 0
        while len(height) > 1:
            id = len(height) - 1 - (height[::-1].index(max(height[1:])))
            spread = id - 1
            dog_water += height[id] * spread - sum(height[1:id])
            height = height[id:]
        return dog_water

class Solution_Two_Pointers: # T:42.87% M: 6.24%
    def trap(self, height: list[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]
        while left < right:
            if maxL <= maxR: # LEFT
                left += 1
                capasity = maxL - height[left]
                if capasity > 0:
                    water += capasity
                if height[left] > maxL:
                    maxL = height[left]
                print("L", height[left], capasity)
            else: # RIGHT
                right -= 1
                capasity = maxR - height[right]
                if capasity > 0:
                    water += capasity
                if height[right] > maxR:
                    maxR = height[right]
                print("R", height[right], capasity)
        return water
    
if __name__=="__main__":
    s = Solution_Two_Pointers()
    r = s.trap([5,5,1,7,1,1,5,2,7,6])
    print(r)