#DFS, runtime complexity is O(n^[r+c]), space complexity is O(1)

class Solution:
    def numIslands(self, g: List[List[str]]) -> int:
        co=0
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]=='1':
                    self.sink(g, i, j)
                    co+=1
        return co
    def sink(self, g, i, j):
        if i<0 or i>len(g)-1 or j<0 or j>len(g[0])-1 or g[i][j]=='0':
            return
        g[i][j]='0'
        #map(self.sink, (g, g, g, g), (i-1, i, i+1, i), (j, j-1, j, j+1)) not correct
        
        self.sink(g, i-1, j)
        self.sink(g, i+1, j)
        self.sink(g, i, j-1)
        self.sink(g, i, j+1)

        '''
        land, curr =0, 0
        m, n= len(grid), len(grid[0])
        grid=[['0' for _ in range(n)]]+grid
        grid=[grid[i]+['0'] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(n):
                if grid[i][j]=='1' and grid[i-1][j]=='1': curr=-1
                elif grid[i][j]=='1' and grid[i-1][j]!='1' and grid[i][j+1]!='1':
                    land+=1+curr
                    curr=0
            curr=0
        return land
        '''