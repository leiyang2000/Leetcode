from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge = [0] * n
        mimp = 0
    
        for road in roads:
            edge[road[0]] += 1
            edge[road[1]] += 1
        
        edge.sort()

        for i in range(len(edge)):
            mimp += edge[i] * (i + 1)
            # 1 2 2 3 4
            # 1 2 3 4 5 value
            # 0 1 2 3 4 (i)
        return mimp




s = Solution()
ret = s.maximumImportance(n = 5, roads = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])
print(ret)


""""
[2, 3, 4, 2, 1]
 0 1 2 3 4

[0,0,0,0,0]
1 1 0 0 0
1 2 1 0 0
1 2 2 1 0
2 2 3 1 0
2 3 3 2 0
2 3 4 2 1


"""