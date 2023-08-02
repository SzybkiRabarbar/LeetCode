from operator import itemgetter
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    # T: 9.69% M: 97.5%
        # for i1,n1 in enumerate(nums):
        #     for i2,n2 in enumerate(nums):
        #         if i1==i2: continue
        #         if n1+n2==target: return [i1,i2]
    # T: 48.57% M: 88.92%
        # for i,n in enumerate(nums):
        #     temp = target-n
        #     templ=nums
        #     templ[i]=""
        #     if temp in templ:
        #         return [i,nums.index(temp)]
    # T: 50.69% M: 99.53%
        for i,n in enumerate(nums):
            temp = target-n
            print(temp)
            if temp in nums:
                if temp==n:
                    result = [id for id, num in enumerate(nums) if num==n]
                    if len(result)>1: return[result[0],result[1]]
                    continue
                return [i,nums.index(temp)]
            


if __name__=="__main__":
    l = [3,2,4]
    t = Solution()
    print(t.twoSum(l,6))