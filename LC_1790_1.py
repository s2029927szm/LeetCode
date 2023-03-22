#The runtime complexity is O(n), space complexity is O(1)

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        l1=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                l1.append(s1[i])
                l1.append(s2[i])
        if len(l1)==0:
            return True
        elif len(l1)==4:
            return True if l1[0]==l1[3] and l1[1]==l1[2] else False
        else: return False