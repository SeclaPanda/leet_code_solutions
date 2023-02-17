class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(nums[i])
            for j in range(i):
                ans[i] += nums[j]
        return ans
    

#after short thinking i'll find another solution
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(1, len(nums)):
            ans.append(nums[i] + ans[i-1])
        return ans
'''