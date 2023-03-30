#we treat n step all combinations as c(n). So: c(n)=c(n-1)+c(n-2), Explanation: if the n-1 step all(most/best)
#combination is c(n-1), as well as c(n-2). So the c(n) can have two combinations as c(n-1) move 1 step,
#and c(n-2) move 2 steps. So it's a Fibonacci Sequence
#runtime complexity is O(n), space complexity is O(n), n is input number
class Solution:
    def climbStairs(self, n: int) -> int:
        l=[1,2]
        if n<=2: return n
        else:
            for i in range(2, n):
                l+=[l[i-1]+l[i-2]]
            return l[-1]

    '''
	#if all step is 1, then counts n. if add 2 from 1 to n//2, then permutate 2 in these (n-num(2))space as A^0(n) + A^1(n-1)
	#+A^2(n-2) + ... + A^(n//2)(n->k): n-k=n//2
	#runtime complexit is O(n^2), space complexity is O(1)
        co=0
        #nn=n//2 if n%2==0 else n//2+1
        c2=1
        while c2*2<=n:
            c1=n-c2
            dvr, dvd=1, 1
            for i in range(1, c2+1):
                dvr*=i
            for j in range(c1, c1-c2, -1):
                dvd*=j
            co+=dvd//dvr
            c2+=1

        return co+1
        


    
    #Recursion, runtime complexity is O(3n), space complexity is O(n)
        return self.DG(n)
        
    def DG(self, n):
        if n==0:
            return 1
        elif n<0:
            return 0
        else:
            return self.DG(n-1)+self.DG(n-2)
    '''