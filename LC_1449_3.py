class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        tar_l=[[float('-inf')]*(target+1) for _ in range(10)]
        #return tar_l
        tar_l[0][0]=0
        re_c=[(i+1,c) for i,c in enumerate(cost)]
        ind=0
        for i, c in reversed(re_c):
            ind+=1
            for j in range(target+1):
                if j<c: tar_l[ind][j]= tar_l[ind-1][j]
                else:
                    tar_l[ind][j]=max( tar_l[ind-1][j], tar_l[ind][j-c]*10+i)
                #tar_l[ind][j]=tar_l[ind-1][j] if j<c else tar_l[ind][j]=max(tar_l[ind-1][j],(tar_l[ind][j-c])*10+i)
                #return tar_l[ind][j],ind,j
        return str(tar_l[-1][-1]) if tar_l[-1][-1]>=0 else "0"

'''
#反思：target list can be 1 dimention
each loop from small target to big one, updating them!

'''
        