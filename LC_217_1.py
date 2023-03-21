#This runtime complexity is O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        lens=len(nums)-1
        while lens:
            if nums[lens]==nums[lens-1]: return True
            else: lens-=1
        return False


#This runtime complexity is O(n^2) as count() is O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for i in nums:
            if nums.count(i)>=2: return True
        return 


#This O(n) transfer the question into if there's repeat items as set() is O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(nums)==len(set(nums)) else True
        


		
		