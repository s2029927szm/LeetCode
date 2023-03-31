#the runtime complexity is O(n^2), space complexity is O(6n), n is the length of input numbers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ne, ze, po, output=[], [], [], set()
        for i in nums:
            if i<0: ne.append(i)
            elif i>0: po.append(i)
            else: ze.append(i)
        NE, PO=set(ne), set(po)
        #0 exist, compare num, -num, 0
        if ze:
            for i in NE:
                if -1*i in PO: output.add((i,0,-1*i))
        #0, 0, 0 exit, add (0,0,0)
        if len(ze)>=3: output.add((0,0,0))
        #2 negative nums qual to 1 positive num
        for i in range(len(ne)-1):
            for j in range(i+1,len(ne)):
                curr=-1*(ne[i]+ne[j])
                if curr in PO: output.add(tuple(sorted([ ne[i],ne[j],curr ])))
        #2 positive nums equal to 1 negative num
        for i in range(len(po)-1):
            for j in range(i+1, len(po)):
                curr=-1*(po[i]+po[j])
                if curr in NE: output.add(tuple(sorted([ po[i],po[j],curr ])))
        return [list(i) for i in output]
        '''
        ll=[]
        nums.append(0)
        nums=sorted(nums, reverse=True)
        #if nums[0]==0 and nums[-1]==0: return [[0,0,0]]
        #num1: positive; num2: negative
        num1=nums[:nums.index(0)]
        num2=nums[nums.index(0)+1:]
        if len(num2)>=3 and num2[2]==0 : ll.append((0,0,0))
        num3, num4=[], []
        for i in range(len(num1)):
            for j in range(i, len(num1)):
                if i!=j:
                    num3.append((num1[i],num1[j]))
        for i in range(len(num2)):
            for j in range(i, len(num2)):
                if i!=j:
                    num4.append((num2[i],num2[j]))
        num3, num4=set(num3), set(num4)
        #print(num3, num4)
        for i in num1:
            for j,k in num4:
                if i+j+k==0:
                    ll.append((i,j,k))
        for i in num2:
            for j,k in num3:
                if i+j+k==0:
                    ll.append((i,j,k))
        ll=list(set(ll))
        return ll
      '''
	  
	  
	#Another workout solution:
	'''
	sorted(nums)
	for i, n in enumerate(nums):
	Le1, Ri1=i+1, len(nums)-1    #从nums[i]右边开始，寻找另外两个加和为0的num
	while Le1<Ri1:               #关门思路寻找和为0的结果
		if n+nums[Le1]+nums[Ri1]==0:
			add((n,nums[Le1],nums[Ri1]))
			Le1+=1
			Ri1-=1
		elif ...<0:              #加和<0，则第二个数太小了，需要左数右移
			Le1+=1
		else:                    #加和>0，则第三个数太大了，需要右数左移
			Ri1-=1
	'''