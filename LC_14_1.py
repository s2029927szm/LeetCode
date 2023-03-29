class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs=sorted(strs)
        i=0
        while i<len(strs[0]):
            if strs[0][i]!=strs[-1][i]: break #add into while with "and"
            i+=1
        return strs[0][:i]
        
        i=0
        ots=''
        lens=len(strs)
        min=len(sorted(strs)[0])
        while i-min:

            for j in range(1,lens):
                if strs[j-1][i]!=strs[j][i]:return ots
            ots+=strs[0][i]
            i+=1
        return ots
