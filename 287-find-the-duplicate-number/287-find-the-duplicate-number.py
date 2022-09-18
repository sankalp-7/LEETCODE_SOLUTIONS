class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=0
        for i in nums:
            dic[i]+=1
        for k,v in dic.items():
            if v>=2:
                return k
        
        