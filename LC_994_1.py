class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        time1=0
        l=[]
        for i in grid:
            l+=i
        le1=len(l)+n
        l=[0 for _ in range(n)]+l+[0 for _ in range(n)]
        co2=0
        #for i in range(m+n):
        while co2!=l.count(2):
            co2=l.count(2)
            if not 1 in l:break
            time1+=1
            tem_l=l.copy()
            for j in range(n,le1):
                if tem_l[j]==2:
                    if j%n==0:
                        # grid in left edge
                        if l[j-n]!=0:l[j-n]=2
                        #if l[j-1]!=0:l[j-1]=2
                        if l[j+1]!=0:l[j+1]=2
                        if l[j+n]!=0:l[j+n]=2
                    elif j%n==n-1:
                        # grid in right edge
                        if l[j-n]!=0:l[j-n]=2
                        if l[j-1]!=0:l[j-1]=2
                        #if l[j+1]!=0:l[j+1]=2
                        if l[j+n]!=0:l[j+n]=2
                    else:
                        # grid not in edge
                        if l[j-n]!=0:l[j-n]=2
                        if l[j-1]!=0:l[j-1]=2
                        if l[j+1]!=0:l[j+1]=2
                        if l[j+n]!=0:l[j+n]=2
        if 1 in l:return -1
        return time1