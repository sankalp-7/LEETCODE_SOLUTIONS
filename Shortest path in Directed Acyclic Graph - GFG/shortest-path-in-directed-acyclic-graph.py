#User function Template for python3

from typing import List
import collections
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        M=m
        N=n
        def toposort(i,vis,adj,stk):
            vis[i]=1
            for node in adj[i]:
                v=node[0]
                if not vis[v]:
                    toposort(v,vis,adj,stk)
            stk.append(i)
            

        adj=collections.defaultdict(list)
        for i in range(M):
            adj[edges[i][0]].append([edges[i][1],edges[i][2]])
        vis=[0 for i in range(N)]
        stk=[]
        for i in range(N):
            if not vis[i]:
                toposort(i,vis,adj,stk)
                
        
        dist=[float("inf") for i in range(N)]
        dist[0]=0
        for i in range(len(stk)):
            top=stk.pop()
            for node in adj[top]:
                if node[1]+dist[top]<dist[node[0]]:
                    dist[node[0]]=node[1]+dist[top]
        for i in range(len(dist)):
            if dist[i]==float("inf"):
                dist[i]=-1
        return dist
            
            
                    
            
        
        
        
            
            
#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends