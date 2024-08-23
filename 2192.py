from typing import List
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[]] * n
        #[[3,4],[3],[4,7],[5,6,7],[6]]
        result = []

        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])

        # def dfs()
            

        for f in range(n):
            anc = []
            

            result.append(anc)

        return result






# dfs!!
# issue??
# read 166