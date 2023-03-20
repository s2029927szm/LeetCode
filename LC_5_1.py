'''
Normally, this question may runs O(n^3) time complexity, as n for all combination start in "s",
n for finding the combination, and n for output the longest

Following runs O(n^2). Using 2 pointers (left and right) to find combinations. The key for this problem
is how to understanding Palindrome! best for simple ways to solve it

Warning: use reverse may cause misleading~~ "abedba" but "ab" or "ba" are not correct; try "abcefcba"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_s=''
        for i in range(len(s)):
            lens=len(s)

            right=0
            while i+right<lens and s[i]==s[i+right]:
                right+=1
            
            left=1
            while i-left>-1 and i+right<lens and s[i-left]==s[i+right]:
                left+=1
                right+=1
            if right+left-1>len(max_s):
                max_s=s[i-left+1:i+right]
        return max_s