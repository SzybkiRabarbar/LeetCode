#https://leetcode.com/problems/contains-duplicate/description/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        temp_dict=dict.fromkeys(nums, False)
        return not len(temp_dict)==len(nums)
        

if __name__=="__main__":
    lst = [1,2,3,4]
    t=Solution()
    print(t.containsDuplicate(lst))
        