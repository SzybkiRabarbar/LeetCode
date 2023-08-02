class Solution(object):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    #T:36.47% M:37%
    def groupAnagrams(self, strs):
        result=[]
        sorted_strs=("".join(sorted(s)) for s in strs)
        content = dict()
        for i,x in enumerate(sorted_strs):
            if not x in content:
                content[x] = [i]
                continue
            content[x].append(i)
        #return [value for value in content.values()]
        for value in content.values():
            result.append([strs[v] for v in value])
        return result

    """
    class Solution(object):
    def groupAnagrams(self, strs):
        dic={}
        for s in strs:
            rev="".join(sorted(s))
            if rev in dic:
                dic[rev].append(s)
            else:
                dic[rev]=[s]
        return dic.values()
    """           
        
        
if __name__=="__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    t = Solution()
    print(t.groupAnagrams(strs))