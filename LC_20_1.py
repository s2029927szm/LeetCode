#The runtime complexity i O(n*3), space complexity is O(1), n mean length o f"s"
class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            '(':')',
            '[':']',
            '{':'}'
        }
        sta=[]
        for i in s: #***** if i in dic: means if i in keys of dic! not values!
            if i in dic: sta.append(i)
            elif sta and dic[sta.pop()]==i: continue
            else: return False
        return not sta #****** Only return None/empty/False here will be recognize as return False
                    
#This runtime complexity is O(n*3+), space complexity is O(1)
class Solution:
    def isValid(self, s: str) -> bool:
		if len(s)%2!=0:return False
		s1='0'
		for i in range(len(s)):
		   if s[i]=='(' or s[i]=='[' or s[i]=='{':
			   s1+=s[i]
		   else:
				if s[i]==')' and s1[-1]=='(':s1=s1[:-1]
				elif s[i]==']' and s1[-1]=='[':s1=s1[:-1]
				elif s[i]=='}' and s1[-1]=='{':s1=s1[:-1]
				else: return False
		if s1=='0':return True
		else: return False
