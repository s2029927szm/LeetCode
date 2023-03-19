#O(n)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ll=[nums[0]]
        for i in nums[1:]:
            ll.append(i+ll[-1])
        return ll


'''
Another O(n!+n)

		return [sum(nums[:i+1]) for i in range(len(nums))]
'''


'''
Use deque as First O(n)

from collections import deque
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lld=deque()
        lld.append(nums[0])
        for i in nums[1:]:
            lld.append(i+lld[-1])
        return lld
'''
