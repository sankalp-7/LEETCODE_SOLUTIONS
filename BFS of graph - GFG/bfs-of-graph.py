#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q=[0]
        
        visited=[0 for x in range(V)]
        
        visited[0]=1
        
        ans=[]
        
        while q:
            vertex=q.pop(0)
            ans.append(vertex)
            for i in adj[vertex]:
                if visited[i]==0:
                    visited[i]=1
                    q.append(i)
        return ans
            
                
                    


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends