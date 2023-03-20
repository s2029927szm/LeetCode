#Binary Search: key is "if target ==/ >/ < nums[mid]", so when
#we narrow down the scope (high = mid -1; low = mid +1)
#we need exlude the mid number out of the new scope as we already
#compared if nums[mid] =target
#O(logn) as 2^n=len(nums)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi= 0, len(nums)-1
        while lo<=hi:
            mid= (hi+lo)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                lo=mid+1
            else:
                hi=mid-1
        return -1
		
#O(n) as index() methods is O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
		return nums.index(target) if target in nums else -1