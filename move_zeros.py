class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums)):
            if nums[i] == 0:
                tmp = nums[i]
                nums.pop(i)
                nums.append(tmp)
        for i in reversed(range(0, len(nums))):
            if nums[i] == 0:
                tmp = nums[i]
                nums.pop(i)
                nums.append(tmp)
        print(nums)