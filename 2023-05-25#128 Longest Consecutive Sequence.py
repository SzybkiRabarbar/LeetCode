class Solution(object):
    def longestConsecutive(self, nums:list):
        """
        :type nums: List[int]
        :rtype: int
        """
        #T: 51.40% M:97.43%
        if not nums: return 0
        nums.sort()
        nums.append(nums[len(nums)-1]-2)
        #print(nums)
        res=0
        temp=1
        for id in range(len(nums)-1):
            if nums[id]==nums[id+1]:
                continue
            elif nums[id]+1==nums[id+1]:
                temp+=1
            else:
                if temp>res:
                    res=temp
                temp=1
        return res

if __name__=="__main__":
    ar=[1,2,0,1]
    print(Solution().longestConsecutive(ar))