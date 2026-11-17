class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found: dict[int,int] = {}
        for i in range(len(nums)):
            if nums[i] in found:
                return[found[nums[i]], i]
            else:
                found[target - nums[i]] = i