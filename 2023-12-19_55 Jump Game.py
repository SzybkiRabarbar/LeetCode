# https://leetcode.com/problems/jump-game/

class Solution1:  # T: 11.64% M: 6.52% O(N^logN)
    def canJump(self, nums: list[int]) -> bool:
        can_jump = [False]*(len(nums) - 1) + [True]
        for i, n in reversed(list(enumerate(nums[:-1]))):
            for j in range(1, n + 1):
                if can_jump[i + j]:
                    can_jump[i] = True
                    break
        return can_jump[0]


class Solution:  # T: 88.08% M: 80.39% O(N)
    # @ https://www.youtube.com/watch?v=Yan0cv2cLy8
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
