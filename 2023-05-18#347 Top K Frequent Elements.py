#https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums:list, k:int)->list:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #T: 73.22% M:69.83%
        '''
        result={}
        for n in nums:
            if not n in result:
                result[n]=1
                continue
            result[n]+=1
        result=sorted(result.items(), key=lambda item: item[1], reverse=True)
        return [result[x][0] for x in range(0,k)]
        '''
        # 73.22% M:69.83%
        result = Counter(nums)
        return [m[0] for m in result.most_common(k)]
if __name__=="__main__":
    nums = [1,1,1,2,2,3,2,2]
    k = 2
    T = Solution()
    print(T.topKFrequent(nums,k))