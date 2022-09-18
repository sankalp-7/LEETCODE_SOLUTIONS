class Solution:
    def trap(self, height: List[int]) -> int:
        max1=0
        pre=[]
        suff=[]
        for i in range(len(height)):
            if height[i]>max1:
                max1=height[i]
            pre.append(max1)
        max1=0
        for i in range(len(height)-1,-1,-1):
            if height[i]>max1:
                max1=height[i]
            suff.append(max1)
        max1=0
        suff=suff[::-1]
        for i in range(len(height)):
            water=min(pre[i],suff[i])-height[i]
            max1+=water
        return max1      