#Runtime complexiy is O(n^2), space complexity is O(*n), n is the length of String "s"
#*n means the unique item in String "s"

class Solution:
    def minDeletions(self, s: str) -> int:
        ll=sorted([s.count(i) for i in set(list(s))], reverse=True)
        curr=ll[0]
        out_l=[ll[0]]
        for i in range(1, len(ll)):
            if curr==0:break
            if ll[i]>=curr:
                curr-=1
                out_l.append(curr)
            else:
                curr=ll[i]
                out_l.append(curr)
        #print(ll,out_l)
        return sum(ll)-sum(out_l)