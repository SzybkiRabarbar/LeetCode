# https://leetcode.com/problems/largest-rectangle-in-histogram/

# class Solution:
#     def largestRectangleArea(self, heights: list[int]) -> int:
#         result = 0
#         for level in range(max(heights),0,-1):
#             streak = 0
#             for position in heights:
#                 if position >= level:
#                     streak += 1
#                 elif streak and (streak * level) > result:
#                     result = streak * level
#                     streak = 0
#                 else:
#                     streak = 0
#             if streak and (streak * level) > result:
#                 result = streak * level
#         return result

class Solution: # T: 99.67%  M: 75.25%
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        for id, height in enumerate(heights):
            if not stack:
                stack.append([id, height])
            elif stack[-1][1] < height:
                stack.append([id, height])
            elif stack[-1][1] > height:
                while stack and stack[-1][1] > height:
                    last = stack.pop()
                    if last[1] * (id - last[0]) > max_area:
                        max_area = last[1] * (id - last[0])
                if not stack or stack[-1][1] < height:
                    stack.append([last[0], height])
        ln = len(heights)
        for val in stack:
            if val[1] * (ln - val[0]) > max_area:
                max_area = val[1] * (ln - val[0])
        return max_area
        
if __name__=="__main__":
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))