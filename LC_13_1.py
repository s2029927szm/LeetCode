#Runtime complexity is O(n), space complexity is O(1), n is length of s.
#Note: expression1 if condition else expression2, 若exp1 has assign, exp2 must not have assign

class Solution:
    def romanToInt(self, s: str) -> int:
        dic={
            'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1
        }
        num=0
        for i in range(len(s)-1):
            num=num-dic[s[i]] if dic[s[i]]<dic[s[i+1]] else num+dic[s[i]]
            '''
                num-=dic[s[i]]
            else:
                num+=dic[s[i]]
            '''
        return num+dic[s[-1]]


#this is more specify, but not essential
        '''
        dic={
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1
        }
        outn=dic[s[0]]
        oldi=s[0]
        for i in range(1, len(s)):
            if dic[oldi]<dic[s[i]]:
                outn+=dic[oldi+s[i]]-dic[oldi]
                oldi='M'
            else:
                outn+=dic[s[i]]
                oldi=s[i]
        return outn
        '''