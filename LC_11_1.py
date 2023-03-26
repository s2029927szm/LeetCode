#Runtime complexity is O(3n), space complexity is O(n), n is length of height
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right= 0, len(height)-1
        max_o=0
        while right-left>0:
            curr=min(height[left], height[right])*(right-left)
            if curr>max_o: max_o=curr
            if height[left] <= height[right]: left+=1
            else: right-=1
        return max_o


#the below method run out of time, but right! runtime complexity is O(n^2), space complexity is O(n^2)
# n is the length of height
        '''
        n=len(height)
        #dp=[[float('-inf')]*(n-1)]*n
        #dp[0][0]=0
        omax=0
        for j in range(1,n):
            for i in range(n):
                if i==j: break
                omax=max( min(height[i],height[j])*(j-i), omax)
        return omax
        '''
        