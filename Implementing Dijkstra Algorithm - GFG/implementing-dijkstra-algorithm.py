import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        dist=[float("inf") for i in range(V)]
        dist[S]=0
        pq=[]
        heapq.heappush(pq,[0,S])
        while pq:
            X=heapq.heappop(pq)
            d=X[0]
            node=X[1]
            for adjnodes in adj[node]:
                if d+adjnodes[1]<dist[adjnodes[0]]:
                    dist[adjnodes[0]]=d+adjnodes[1]
                    heapq.heappush(pq,[dist[adjnodes[0]],adjnodes[0]])
        return dist
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends