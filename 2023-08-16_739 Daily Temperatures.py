# https://leetcode.com/problems/daily-temperatures/description/

class Solution: # T:97.72% M: 79.73%
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result, stack = [0 for _ in range(len(temperatures))], []
        for id, farenheit in enumerate(temperatures):
            while stack and farenheit > stack[-1][0]:
                s_farenheit, s_id = stack.pop()
                result[s_id] = (id - s_id)
            stack.append((farenheit, id))
        return result
        
if __name__=="__main__":
    s = Solution()
    print(s.dailyTemperatures([100,65,67,52,63,40,92,44,66,39]))