class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found: dict[int,int] = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in found:
                return[found[num], i]
            else:
                found[target - num] = i