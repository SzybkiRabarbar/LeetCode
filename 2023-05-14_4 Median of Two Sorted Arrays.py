# https://leetcode.com/problems/median-of-two-sorted-arrays/
from numpy import median

class Solution(object):
    def findMedianSortedArrays(self, nums1:list, nums2:list) -> float:
        #isinstance(n,str)
        n1,n2="",""
        result=[]
        while len(nums1)+len(nums2) or not isinstance(n1,str) or not isinstance(n2,str):
            #print(f"Before: 1-{n1} 2-{n2}")
            if isinstance(n1,str) and len(nums1): n1= nums1.pop(0)
            if isinstance(n2,str) and len(nums2): n2= nums2.pop(0)
            if isinstance(n1,str) and isinstance(n2,str): break
            #print(f"After: 1-{n1} 2-{n2}")
            if isinstance(n1,str):
                result.append(n2)
                n2=""
                continue
            if isinstance(n2,str):
                result.append(n1)
                n1=""
                continue
            if n1>n2:
                result.append(n2)
                n2=""
            else:
                result.append(n1)
                n1=""
        return median(result)
                
if __name__=="__main__":
    S = Solution()
    print(S.findMedianSortedArrays([1,3],[2]))
