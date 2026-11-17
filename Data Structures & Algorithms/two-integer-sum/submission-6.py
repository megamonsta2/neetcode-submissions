class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if nums[i] + nums[j] == target: return [i,j]
        # last = len(nums) - 1
        # one, two = 0, last
        # while True:
        #     result = nums[one] + nums[two]
        #     print(one,two,nums[one],nums[two],result)
        #     if result == target:
        #         return [one, two]
        #     elif (target >= 0 and result > target) or (target < 0 and result < target):
        #         two -= 1
        #     elif (target >= 0 and result < target) or (target < 0 and result > target):
        #         one += 1
        #         two = last