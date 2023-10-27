# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution: 
    def twoSum1(self, numbers: list[int], target: int) -> list[int]: ## T: 5.4% M: 99.69%
        for id, n1 in enumerate(numbers):
            if n1 in numbers[:id]:
                continue
            for diff, n2 in enumerate(numbers[id+1::]):
                if n1 + n2 == target:
                    return [id+1, id+2+diff]

    def twoSum(self, numbers: list[int], target: int) -> list[int]: ## T: 86.03% M: 60.71%
        left = 0
        right = len(numbers) - 1
        while True:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
                
if __name__=="__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15],9))
    print(s.twoSum([2,3,4],6))