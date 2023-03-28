#runtime complexity is O(n), space complexity is O(n), n is the length of list(intervals)
#Note: sorted() only compare the first sub-item of the items in iterable object!
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        lsort=sorted(intervals)
        #lsort=sorted(intervals, key=lambda x:x[0], reverse=False)
        lout=[[-1,-1]]
        for i in range(len(lsort)):
            if lsort[i][0]>=lout[-1][0] and lsort[i][0]<=lout[-1][1] and lsort[i][1]>lout[-1][1]: lout[-1][1]=lsort[i][1]
            elif lsort[i][0]>lout[-1][1]: lout.append(lsort[i])
        return lout[1:]