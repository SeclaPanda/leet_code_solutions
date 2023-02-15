class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set the left and right boundaries
        left = 0
        right = len(nums)
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1

#below is work solution, but not the binary search
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in nums: 
            if target == i:
                    return nums.index(i)
        else:
            return -1
'''