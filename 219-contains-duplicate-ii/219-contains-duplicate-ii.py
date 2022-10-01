class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		count={}
		for i,n in enumerate(nums):
			if(n in count.keys() and i-count[n][1]<=k):
					return True
			count[n]=[1,i]
		return False